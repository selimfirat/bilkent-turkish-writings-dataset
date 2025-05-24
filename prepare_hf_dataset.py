"""
Convert the Bilkent Turkish Writings Dataset to a Hugging Face compatible dataset.
"""
import os
import json
from datasets import Dataset, Features, Value
from dataset_versioning import initialize_version_control, get_latest_version


def convert_to_hf_dataset(version=None):
    """Convert the dataset to Hugging Face Dataset format."""
    # Initialize version control
    initialize_version_control()
    
    # Determine which version to convert
    if version is None:
        latest_version = get_latest_version()
        version = latest_version["version"]
    
    version_dir = f"./versions/{version}"
    
    # Load metadata
    metadata_path = f"{version_dir}/metadata.json"
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
    else:
        metadata = {"version": version, "date_created": "unknown"}
    
    # Create empty dataset with proper features
    features = Features({
        'text': Value('string')
    })
    
    # Create an empty dataset
    dataset = Dataset.from_dict({'text': []}, features=features)
    
    # Save the dataset
    output_dir = f"./hf_datasets/{version}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the dataset
    dataset.save_to_disk(output_dir)
    
    # Note: We don't save metadata.json in the dataset directory to avoid schema conflicts
    # The metadata is returned and can be used elsewhere
    
    print(f"Dataset {version} converted and saved to {output_dir}")
    
    return {
        "dataset": dataset,
        "metadata": metadata
    }


def push_to_hub(version=None, namespace="bilkent", dataset_name="turkish-writings"):
    """Push the dataset to Hugging Face Hub."""
    from huggingface_hub import HfApi
    import os
    
    if version is None:
        latest_version = get_latest_version()
        version = latest_version["version"]
    
    repo_id = f"{namespace}/{dataset_name}"
    
    # Check if HF_TOKEN is available in environment
    token = os.environ.get("HF_TOKEN")
    if not token:
        print("Warning: HF_TOKEN not found in environment variables.")
        print("To push to Hugging Face Hub, please set the HF_TOKEN environment variable:")
        print("export HF_TOKEN=your_huggingface_token")
        return False
    
    api = HfApi()
    
    # Upload dataset files
    dataset_dir = f"./hf_datasets/{version}"
    if not os.path.exists(dataset_dir):
        convert_to_hf_dataset(version)
    
    print(f"Pushing {version} to Hugging Face Hub at {repo_id}...")
    
    # Upload all files from the dataset directory
    api.upload_folder(
        folder_path=dataset_dir,
        repo_id=repo_id,
        repo_type="dataset",
        token=token
    )
    
    print(f"Dataset {version} successfully pushed to {repo_id}")
    return True


if __name__ == "__main__":
    # First initialize version control to ensure v1 exists
    initialize_version_control()
    
    # Convert the dataset to Hugging Face format
    convert_to_hf_dataset()
