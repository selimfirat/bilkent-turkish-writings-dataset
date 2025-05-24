#!/usr/bin/env python
"""
Update the Bilkent Turkish Writings Dataset and release a new version.
"""
import os
import argparse
import subprocess
from dataset_versioning import initialize_version_control, get_latest_version, create_new_version
from prepare_hf_dataset import convert_to_hf_dataset, push_to_hub


def run_scraper():
    """Run the scraper to get the latest data."""
    print("Running the scraper to collect the latest data...")
    os.makedirs("./data", exist_ok=True)
    
    # Change directory to the scraper folder
    os.chdir("./scraper")
    
    # Run the scrapy crawler
    try:
        subprocess.run(["scrapy", "crawl", "bilkent_turkish_writings"], check=True)
        print("Scraper completed successfully")
        os.chdir("../")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running scraper: {e}")
        os.chdir("../")
        return False


def convert_to_text():
    """Run the conversion script to convert PDFs to text."""
    print("Converting PDFs to text...")
    try:
        subprocess.run(["python", "convert_to_text.py"], check=True)
        print("Conversion completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting PDFs to text: {e}")
        return False


def update_dataset(version_num=None, push=False, skip_scraper=True):
    """Update the dataset with the latest data and create a new version."""
    # Initialize version control to ensure v1 exists
    latest = initialize_version_control()
    print(f"Current version: {latest['version']}")
    
    # Determine the next version number
    if version_num is None:
        if latest:
            current_num = int(latest["version"][1:])  # Extract number from "v1", "v2", etc.
            version_num = current_num + 1
        else:
            version_num = 1
    
    print(f"Preparing to create version v{version_num}")
    
    # Skip scraper and PDF conversion if flag is set (useful for testing)
    if not skip_scraper:
        # Run the scraper to get the latest data
        if not run_scraper():
            print("Failed to run scraper. Update aborted.")
            return False
        
        # Convert PDFs to text
        if not convert_to_text():
            print("Failed to convert PDFs to text. Update aborted.")
            return False
    
    # Create a new version
    new_version = create_new_version(version_num)
    print(f"Created new version: {new_version['version']}")
    
    # Convert to Hugging Face dataset format
    try:
        convert_to_hf_dataset(new_version['version'])
        print(f"Successfully converted {new_version['version']} to Hugging Face format")
    except Exception as e:
        print(f"Error converting to Hugging Face format: {e}")
        return False
    
    # Push to Hugging Face Hub if requested
    if push:
        try:
            push_result = push_to_hub(new_version['version'])
            if push_result:
                print(f"Successfully pushed {new_version['version']} to Hugging Face Hub")
            else:
                print("Failed to push to Hugging Face Hub. Check if HF_TOKEN is set.")
        except Exception as e:
            print(f"Error pushing to Hugging Face Hub: {e}")
    
    print(f"Dataset update to {new_version['version']} completed successfully!")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update the Bilkent Turkish Writings Dataset")
    parser.add_argument(
        "--version", 
        type=int, 
        help="Version number for the new dataset (default: increment the latest version)"
    )
    parser.add_argument(
        "--push", 
        action="store_true", 
        help="Push the dataset to Hugging Face Hub after updating"
    )
    parser.add_argument(
        "--run-scraper",
        action="store_true",
        help="Run the scraper to collect new data (not needed for testing)"
    )
    args = parser.parse_args()
    
    update_dataset(args.version, args.push, not args.run_scraper)
