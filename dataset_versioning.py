"""
Dataset versioning utilities for Bilkent Turkish Writings Dataset.
"""
import os
import shutil
import json
import pandas as pd
from datetime import datetime


def initialize_version_control():
    """Initialize the version control system."""
    version_info_dir = "./versions"
    os.makedirs(version_info_dir, exist_ok=True)
    
    # Check if we need to create a v1 from existing data
    if not os.path.exists(f"{version_info_dir}/v1"):
        print("Creating initial version (v1) from existing dataset...")
        
        # Create version directory
        os.makedirs(f"{version_info_dir}/v1", exist_ok=True)
        
        # Copy current data to v1
        if os.path.exists("./data/texts.csv"):
            shutil.copy("./data/texts.csv", f"{version_info_dir}/v1/texts.csv")
        
        # Create version metadata
        metadata = {
            "version": "v1",
            "date_created": datetime.now().strftime("%Y-%m-%d"),
            "num_entries": count_entries(f"{version_info_dir}/v1/texts.csv"),
            "description": "Initial version of Bilkent Turkish Writings Dataset"
        }
        
        with open(f"{version_info_dir}/v1/metadata.json", 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        
        print(f"Version v1 created with {metadata['num_entries']} entries")
    
    return get_latest_version()


def create_new_version(version_num):
    """Create a new version of the dataset."""
    version_info_dir = "./versions"
    version_name = f"v{version_num}"
    
    # Ensure versions directory exists
    os.makedirs(version_info_dir, exist_ok=True)
    
    # Create version directory
    os.makedirs(f"{version_info_dir}/{version_name}", exist_ok=True)
    
    # Copy current data to new version
    if os.path.exists("./data/texts.csv"):
        shutil.copy("./data/texts.csv", f"{version_info_dir}/{version_name}/texts.csv")
    
    # Create version metadata
    metadata = {
        "version": version_name,
        "date_created": datetime.now().strftime("%Y-%m-%d"),
        "num_entries": count_entries(f"{version_info_dir}/{version_name}/texts.csv"),
        "description": f"Version {version_name} of Bilkent Turkish Writings Dataset"
    }
    
    with open(f"{version_info_dir}/{version_name}/metadata.json", 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print(f"Version {version_name} created with {metadata['num_entries']} entries")
    return metadata


def get_latest_version():
    """Get information about the latest version."""
    version_info_dir = "./versions"
    
    if not os.path.exists(version_info_dir):
        return None
    
    versions = [d for d in os.listdir(version_info_dir) if d.startswith('v') and os.path.isdir(os.path.join(version_info_dir, d))]
    
    if not versions:
        return None
    
    # Sort versions and get the latest one
    versions.sort(key=lambda x: int(x[1:]))
    latest = versions[-1]
    
    metadata_path = os.path.join(version_info_dir, latest, "metadata.json")
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    return {"version": latest, "date_created": "unknown", "num_entries": "unknown"}


def count_entries(csv_path):
    """Count the number of entries in a CSV file."""
    if not os.path.exists(csv_path):
        return 0
    
    try:
        df = pd.read_csv(csv_path)
        return len(df)
    except:
        return 0


if __name__ == "__main__":
    # For testing purposes
    latest = initialize_version_control()
    print(f"Latest version: {latest}")
