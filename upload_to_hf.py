#!/usr/bin/env python3
"""
Clean upload script that avoids schema conflicts by uploading datasets directly.
"""
import os
import json
import pandas as pd
from datasets import Dataset, Features, Value
from huggingface_hub import HfApi
from dataset_versioning import initialize_version_control


def create_dataset_card(version, metadata):
    """Create a README.md file (dataset card) for the HF dataset."""
    card_content = f"""---
license: other
license_name: "academic-use-only"
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

# Load the latest version (v2) - default configuration
dataset = load_dataset("selimfirat/bilkent-turkish-writings-dataset")

# Access the data
for item in dataset['train'].take(5):
    print(f"Text: {{item['text'][:100]}}...")
    print("---")

# Create custom splits if needed
split_dataset = dataset['train'].train_test_split(test_size=0.2)
train_data = split_dataset["train"]
test_data = split_dataset["test"]
```

### Version Information

This dataset provides multiple configurations:

- **Default (v2)**: Latest dataset with 9,119 entries (2014-2025) - **Recommended**
- **v1**: Original dataset with 6,844 entries (2014-2018)
- **v2**: Same as default, explicitly named configuration

### Accessing Different Versions

```python
from datasets import load_dataset

# Method 1: Load default version (v2 - recommended)
dataset = load_dataset("selimfirat/bilkent-turkish-writings-dataset")

# Method 2: Explicitly load v2 configuration
dataset_v2 = load_dataset("selimfirat/bilkent-turkish-writings-dataset", "v2")

# Method 3: Load v1 configuration (original version)
dataset_v1 = load_dataset("selimfirat/bilkent-turkish-writings-dataset", "v1")

# All methods above return the same structure
print(f"Number of entries: {{len(dataset['train'])}}")
print(f"First text preview: {{dataset['train'][0]['text'][:100]}}...")
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
- **Dataset Compiler**: Selim F. Yilmaz for collecting, processing, and structuring the dataset

## Contact

For questions or issues, please visit the [GitHub repository](https://github.com/selimfirat/bilkent-turkish-writings-dataset).
"""
    return card_content


def load_and_upload_dataset(version, repo_id="selimfirat/bilkent-turkish-writings-dataset", config_name=None, as_default=False):
    """Load CSV data and upload directly to Hugging Face Hub."""
    # Check HF token
    token = os.environ.get("HF_TOKEN")
    if not token:
        print("Error: HF_TOKEN not found in environment variables.")
        return False
    
    # Load CSV data
    version_dir = f"./versions/{version}"
    csv_path = f"{version_dir}/texts.csv"
    
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return False
    
    print(f"Loading {csv_path}...")
    df = pd.read_csv(csv_path, encoding='utf-8')
    print(f"Loaded {len(df)} entries from {version}")
    
    # Clean data: only keep text column
    if 'text' not in df.columns:
        print(f"Error: 'text' column not found in {csv_path}")
        return False
    
    text_df = pd.DataFrame({'text': df['text'].fillna('')})
    
    # Create HF dataset
    features = Features({'text': Value('string')})
    dataset = Dataset.from_pandas(text_df, features=features)
    
    # Load metadata
    metadata_path = f"{version_dir}/metadata.json"
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
    else:
        metadata = {"version": version, "date_created": "unknown", "num_entries": len(dataset)}
    
    # Create dataset card only for default upload
    if as_default:
        card_content = create_dataset_card(version, metadata)
    
    config_desc = "as default" if as_default else f"with config '{config_name}'"
    print(f"Uploading {version} {config_desc} to {repo_id}...")
    
    try:
        # Upload dataset
        if as_default:
            # Upload as default configuration (no config_name)
            dataset.push_to_hub(
                repo_id=repo_id,
                token=token,
                commit_message=f"Upload {version} as default configuration"
            )
        else:
            # Upload with specific config_name
            dataset.push_to_hub(
                repo_id=repo_id,
                config_name=config_name,
                token=token,
                commit_message=f"Upload {version} configuration"
            )
        
        # Upload README only for default upload
        if as_default:
            api = HfApi()
            api.upload_file(
                path_or_fileobj=card_content.encode('utf-8'),
                path_in_repo="README.md",
                repo_id=repo_id,
                repo_type="dataset",
                token=token,
                commit_message=f"Update README for {version}"
            )
        
        config_msg = "as default" if as_default else f"with config '{config_name}'"
        print(f"✅ Successfully uploaded {version} {config_msg} to {repo_id}")
        return True
        
    except Exception as e:
        config_msg = "as default" if as_default else f"with config '{config_name}'"
        print(f"❌ Error uploading {version} {config_msg}: {e}")
        return False


def main():
    """Upload dataset versions: v2 as default and both v1, v2 as named configurations."""
    print("🚀 Starting upload of Bilkent Turkish Writings Dataset...")
    
    # Initialize version control
    initialize_version_control()
    
    # Create fresh repository
    token = os.environ.get("HF_TOKEN")
    if not token:
        print("Error: HF_TOKEN not found.")
        return
    
    repo_id = "selimfirat/bilkent-turkish-writings-dataset"
    api = HfApi()
    
    try:
        # Delete existing repo to start fresh
        api.delete_repo(repo_id=repo_id, repo_type="dataset", token=token)
        print("🗑️ Deleted existing repository")
    except Exception:
        pass
    
    try:
        # Create new repo
        api.create_repo(repo_id=repo_id, repo_type="dataset", token=token, exist_ok=True)
        print("📁 Created new repository")
    except Exception as e:
        print(f"Repository creation info: {e}")
    
    # Upload v2 as default configuration (shows in dataset viewer)
    print("\n📦 Uploading v2 as default configuration...")
    success_v2_default = load_and_upload_dataset("v2", repo_id, as_default=True)
    
    # Upload v1 as named configuration
    print("\n📦 Uploading v1 as named configuration...")
    success_v1 = load_and_upload_dataset("v1", repo_id, config_name="v1")
    
    # Upload v2 as named configuration
    print("\n📦 Uploading v2 as named configuration...")
    success_v2_named = load_and_upload_dataset("v2", repo_id, config_name="v2")
    
    # Summary
    print("\n📊 Upload Summary:")
    print(f"v2 (default): {'✅ Success' if success_v2_default else '❌ Failed'}")
    print(f"v1 (config): {'✅ Success' if success_v1 else '❌ Failed'}")
    print(f"v2 (config): {'✅ Success' if success_v2_named else '❌ Failed'}")
    
    if success_v2_default and success_v1 and success_v2_named:
        print("\n🎉 All uploads completed successfully!")
        print(f"🔗 Dataset available at: https://huggingface.co/datasets/{repo_id}")
        print("📋 Access methods:")
        print("   - Default (v2): load_dataset(repo_id)")
        print("   - v1: load_dataset(repo_id, 'v1')")
        print("   - v2: load_dataset(repo_id, 'v2')")
        print("\n💡 Dataset viewer will show v2 by default")
    else:
        print("\n⚠️ Some uploads failed. Please check the errors above.")


if __name__ == "__main__":
    main()
