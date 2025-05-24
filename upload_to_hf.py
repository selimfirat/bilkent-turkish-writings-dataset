#!/usr/bin/env python3
"""
Upload the Compilation of Bilkent Turkish Writings Dataset to Hugging Face Hub.
This script properly converts CSV data to HF format and uploads both v1 and v2.
"""
import os
import json
import pandas as pd
from datasets import Dataset, Features, Value
from huggingface_hub import HfApi
from dataset_versioning import initialize_version_control, get_latest_version


def load_csv_to_hf_dataset(version):
    """Load CSV data and convert to Hugging Face Dataset format."""
    version_dir = f"./versions/{version}"
    csv_path = f"{version_dir}/texts.csv"
    
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return None
    
    # Load the CSV file
    print(f"Loading {csv_path}...")
    df = pd.read_csv(csv_path, encoding='utf-8')
    print(f"Loaded {len(df)} entries from {version}")
    
    # Define features schema
    features = Features({
        'text': Value('string'),
        'course': Value('string'),
        'semester': Value('string'),
        'author': Value('string'),
        'title': Value('string'),
        'metadata': Value('string'),
        'url': Value('string'),
        'file_id': Value('string')
    })
    
    # Handle missing values
    df = df.fillna('')
    
    # Convert to HF dataset (no splits, just return the full dataset)
    dataset = Dataset.from_pandas(df, features=features)
    
    return dataset


def save_hf_dataset(dataset, version):
    """Save the HF dataset to disk."""
    output_dir = f"./hf_datasets/{version}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the dataset
    dataset.save_to_disk(output_dir)
    
    # Load and save metadata
    metadata_path = f"./versions/{version}/metadata.json"
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        with open(f"{output_dir}/metadata.json", 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print(f"Dataset {version} saved to {output_dir}")
    return output_dir


def create_dataset_card(version, metadata):
    """Create a README.md file (dataset card) for the HF dataset."""
    card_content = f"""---
license: other
license_name: "Academic Use Only"
license_link: "https://github.com/selimfirat/bilkent-turkish-writings-dataset/blob/main/LICENSE"
language:
- tr
size_categories:
- 1K<n<10K
task_categories:
- text-generation
- text-classification
- feature-extraction
pretty_name: "Compilation of Bilkent Turkish Writings Dataset"
tags:
- turkish
- creative-writing
- educational
- nlp
- corpus
- bilkent-university
---

# Compilation of Bilkent Turkish Writings Dataset

## Dataset Description

This is a comprehensive compilation of Turkish creative writings from Bilkent University's Turkish 101 and Turkish 102 courses (2014-2025). The dataset contains **{metadata.get('num_entries', 'N/A')} student writings** originally created by students and instructors, focusing on creativity, content, composition, grammar, spelling, and punctuation development.

**Note**: This dataset is a compilation and digitization of publicly available writings from Bilkent University. The original content was created by students and instructors of the Turkish Department. The dataset compilation, processing, and distribution tools were developed by Selim F. Yilmaz.

## Dataset Information

- **Version**: {version}
- **Date Created**: {metadata.get('date_created', 'N/A')}
- **Number of Entries**: {metadata.get('num_entries', 'N/A')}
- **Language**: Turkish
- **License**: Academic Use Only
- **Original Source**: [Bilkent University Turkish Department](https://stars.bilkent.edu.tr/turkce/)

## Dataset Structure

### Data Fields

- **text**: The full text content of the writing
- **course**: Course identifier (Turkish 101 or Turkish 102)
- **semester**: Academic semester information
- **author**: Anonymized student identifier
- **title**: Writing title (when available)
- **metadata**: Additional contextual information
- **url**: Original source URL (when available)
- **file_id**: Internal file identifier

### Data Splits

This dataset is provided as a single dataset without predefined splits. You can create your own splits as needed:

```python
# Create custom splits if needed
dataset = dataset.train_test_split(test_size=0.2)
train_data = dataset["train"]
test_data = dataset["test"]
```

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("selimfirat/bilkent-turkish-writings-datasets")

# Access the data
for example in dataset.take(5):
    print(f"Title: {example['title']}")
    print(f"Course: {example['course']}")
    print(f"Text: {example['text'][:100]}...")
    print("---")

# Create custom splits if needed
split_dataset = dataset.train_test_split(test_size=0.2)
train_data = split_dataset["train"]
test_data = split_dataset["test"]
```

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{{yilmaz_bilkent_turkish_writings_2025,
  title={{Compilation of Bilkent Turkish Writings Dataset}},
  author={{Yilmaz, Selim F.}},
  year={{2025}},
  publisher={{Zenodo}},
  doi={{10.5281/zenodo.15498155}},
  url={{https://doi.org/10.5281/zenodo.15498155}},
  version={{{version}}},
  note={{Compilation of Turkish creative writings from Bilkent University Turkish 101 and 102 courses (2014-2025). Original content by Bilkent University students and instructors.}}
}}
```

## License

This dataset is released under an **Academic Use License**. Commercial use is prohibited. See the [LICENSE](https://github.com/selimfirat/bilkent-turkish-writings-dataset/blob/main/LICENSE) file for full details.

## Acknowledgments

- **Original Content Creators**: Students and instructors of Turkish 101 and 102 courses at Bilkent University (2014-2025)
- **Bilkent University Turkish Department** for creating and publishing the original writings
- **Dataset Compiler**: Selim F. Yilmaz for collecting, processing, structuring, and distributing the dataset

## Contact

For questions or issues, please visit the [GitHub repository](https://github.com/selimfirat/bilkent-turkish-writings-dataset).
"""
    return card_content


def upload_to_hf(version, namespace="selimfirat", dataset_name="bilkent-turkish-writings-datasets"):
    """Upload a specific version to Hugging Face Hub."""
    # Check if HF_TOKEN is available
    token = os.environ.get("HF_TOKEN")
    if not token:
        print("Error: HF_TOKEN not found in environment variables.")
        print("Please set your Hugging Face token:")
        print("export HF_TOKEN=your_huggingface_token")
        print("You can get a token from https://huggingface.co/settings/tokens")
        return False
    
    # Load and convert the dataset
    print(f"Converting {version} to Hugging Face format...")
    dataset = load_csv_to_hf_dataset(version)
    if dataset is None:
        return False
    
    # Save to disk
    output_dir = save_hf_dataset(dataset, version)
    
    # Load metadata for dataset card
    metadata_path = f"./versions/{version}/metadata.json"
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
    else:
        metadata = {"version": version, "date_created": "unknown", "num_entries": len(dataset)}
    
    # Create dataset card
    card_content = create_dataset_card(version, metadata)
    with open(f"{output_dir}/README.md", 'w', encoding='utf-8') as f:
        f.write(card_content)
    
    # Upload to HF Hub
    repo_id = f"{namespace}/{dataset_name}"
    api = HfApi()
    
    try:
        print(f"Uploading {version} to Hugging Face Hub at {repo_id}...")
        
        # Create the repository if it doesn't exist
        try:
            api.create_repo(repo_id=repo_id, repo_type="dataset", token=token, exist_ok=True)
        except Exception as e:
            print(f"Repository creation warning: {e}")
        
        # Upload all files from the dataset directory
        api.upload_folder(
            folder_path=output_dir,
            repo_id=repo_id,
            repo_type="dataset",
            token=token,
            commit_message=f"Upload {version} of Compilation of Bilkent Turkish Writings Dataset"
        )
        
        print(f"✅ Successfully uploaded {version} to {repo_id}")
        print(f"🔗 View at: https://huggingface.co/datasets/{repo_id}")
        return True
        
    except Exception as e:
        print(f"❌ Error uploading {version}: {e}")
        return False


def main():
    """Main function to upload both v1 and v2 datasets."""
    print("🚀 Starting upload of Compilation of Bilkent Turkish Writings Dataset to Hugging Face...")
    
    # Initialize version control
    initialize_version_control()
    
    # Upload v1
    print("\n📦 Uploading v1...")
    success_v1 = upload_to_hf("v1")
    
    # Upload v2
    print("\n📦 Uploading v2...")
    success_v2 = upload_to_hf("v2")
    
    # Summary
    print("\n📊 Upload Summary:")
    print(f"v1: {'✅ Success' if success_v1 else '❌ Failed'}")
    print(f"v2: {'✅ Success' if success_v2 else '❌ Failed'}")
    
    if success_v1 and success_v2:
        print("\n🎉 All uploads completed successfully!")
        print("🔗 Dataset available at: https://huggingface.co/datasets/selimfirat/bilkent-turkish-writings-datasets")
    else:
        print("\n⚠️  Some uploads failed. Please check the errors above.")


if __name__ == "__main__":
    main()
