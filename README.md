# Compilation of Bilkent Turkish Writings Dataset

[![Dataset](https://img.shields.io/badge/Dataset-Bilkent%20Turkish%20Writings-blue)](https://github.com/selimfirat/bilkent-turkish-writings-dataset)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15498155.svg)](https://doi.org/10.5281/zenodo.15498155)
[![License](https://img.shields.io/badge/License-Academic%20Use-green)](LICENSE)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Datasets-yellow)](https://huggingface.co/datasets/selimfirat/bilkent-turkish-writings-dataset)

A comprehensive collection of Turkish creative writings from Bilkent University's Turkish 101 and Turkish 102 courses since 2014. This dataset contains **9,119 student writings** originally created by students and instructors, focusing on creativity, content, composition, grammar, spelling, and punctuation development. 

**Note**: This dataset is a compilation and digitization of publicly available writings from Bilkent University. The original content was created by students and instructors of the Turkish Department. The dataset compilation, processing, and distribution tools were developed by Selim F. Yilmaz.

## 📊 Dataset Overview (v2)

- **Size**: 9,119 writings (~45MB in CSV format)
- **Language**: Turkish  
- **Domain**: Creative writing, academic writing
- **Format**: Multiple formats available (CSV, Hugging Face Datasets)
- **Source**: [Bilkent University Turkish Department](https://stars.bilkent.edu.tr/turkce/) (Original Content Creator)
- **Compiler**: Selim F. Yilmaz (Dataset Collection & Processing)
- **Publisher**: Zenodo
- **License**: Academic Use Only
- **DOI**: [10.5281/zenodo.15498155](https://doi.org/10.5281/zenodo.15498155)
- **Latest Version**: v2 (May 2025)

### Features
- **Comprehensive Coverage**: Student creative writings spanning multiple academic years
- **Rich Metadata**: Structured information including course details, semester, and authorship
- **Quality Content**: Writings with instructor feedback focusing on creativity and language skills
- **Multiple Formats**: Available in CSV, Hugging Face Datasets, and raw text formats
- **Version Control**: Systematic versioning for dataset tracking and reproducibility
- **Research Ready**: Pre-processed and structured for immediate use in NLP and educational research
- **Continuous Updates**: Regular updates with new semester publications
- **Open Access**: Freely available for academic and research purposes

## Dataset Versions

This dataset follows semantic versioning to track changes and growth over time:

- **v1**: Initial release containing 6,844 writings from the original collection
- **v2**: Current version with 9,119 writings (33% increase) - includes additional content scraped and processed
- **Future versions**: Planned regular updates as new semester content becomes available

Each version maintains backward compatibility and includes detailed changelogs for transparency.

## 📥 Direct Downloads

For quick access to the dataset files:

### CSV Files
- **v2 (Latest)**: [`versions/v2/texts.csv`](versions/v2/texts.csv) - 9,119 writings (~45MB)
- **v1**: [`versions/v1/texts.csv`](versions/v1/texts.csv) - 6,844 writings (~33MB)

### Raw Download URLs
```bash
# Download v2 (latest) directly
wget https://raw.githubusercontent.com/selimfirat/bilkent-turkish-writings-dataset/main/versions/v2/texts.csv

# Download v1 directly  
wget https://raw.githubusercontent.com/selimfirat/bilkent-turkish-writings-dataset/main/versions/v1/texts.csv
```

### Version Metadata
- **v2 metadata**: [`versions/v2/metadata.json`](versions/v2/metadata.json)
- **v1 metadata**: [`versions/v1/metadata.json`](versions/v1/metadata.json)

## 📚 About Turkish 101 & 102 at Bilkent University

These courses are designed as a two-course sequence to develop students' creative writing skills in Turkish through active learning. Key features include:

- **Interactive Learning**: Students maintain personal blogs with regular writing assignments
- **Comprehensive Feedback**: Instructors provide detailed comments on creativity, content, composition, grammar, spelling, and punctuation
- **Skill Development**: Focus on improving Turkish language proficiency and creative expression
- **Public Sharing**: Selected exceptional writings are published publicly each semester

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/selimfirat/bilkent-turkish-writings-dataset.git
cd bilkent-turkish-writings-dataset
pip install -r requirements.txt
```

### Loading the Dataset

#### Option 1: CSV Format (Recommended for basic use)

**Direct Download:**
- **Latest (v2)**: [`versions/v2/texts.csv`](versions/v2/texts.csv) - 9,119 writings
- **Previous (v1)**: [`versions/v1/texts.csv`](versions/v1/texts.csv) - 6,844 writings

```bash
# Download latest version directly
wget https://raw.githubusercontent.com/selimfirat/bilkent-turkish-writings-dataset/main/versions/v2/texts.csv

# Or download specific version
wget https://raw.githubusercontent.com/selimfirat/bilkent-turkish-writings-dataset/main/versions/v1/texts.csv

# After cloning the repository
cp ./versions/v2/texts.csv your_target_path/

# Get version information programmatically
python -c "from dataset_versioning import get_latest_version; print(get_latest_version()['version'])"
```

#### Option 2: Hugging Face Datasets Format (Recommended for ML/NLP)

```python
from datasets import load_from_disk

# Load from local copy (after cloning)
dataset = load_from_disk("./hf_datasets/v2")

# Or load directly from Hugging Face Hub
from datasets import load_dataset
dataset = load_dataset("selimfirat/bilkent-turkish-writings-dataset")

# Access train/validation/test splits
print(f"Train: {len(dataset['train'])} samples")
print(f"Validation: {len(dataset['validation'])} samples") 
print(f"Test: {len(dataset['test'])} samples")
```

#### Option 3: Zenodo Repository (Recommended for archival access)

```bash
# Download directly from Zenodo
wget https://zenodo.org/record/15498155/files/bilkent-turkish-writings-dataset.zip
unzip bilkent-turkish-writings-dataset.zip
```

#### Option 4: Python API

```python
import pandas as pd
from dataset_versioning import get_latest_version

# Get latest version info
latest = get_latest_version()
print(f"Latest version: {latest['version']} with {latest['num_entries']} entries")

# Load as pandas DataFrame
df = pd.read_csv(f"./versions/{latest['version']}/texts.csv")
print(df.head())
```

## 🔄 Dataset Maintenance

### Updating to a New Version

For dataset maintainers to create new versions with additional scraped content:

```bash
# Update dataset and create a new version
python update_dataset.py

# Push to Hugging Face Hub (requires HF_TOKEN environment variable)
python update_dataset.py --push

# Specify version number explicitly
python update_dataset.py --version 3
```

### Full Scraping from Scratch

To recreate the dataset completely from the source:

```bash
# Navigate to scraper directory and run
cd scraper
scrapy crawl bilkent_turkish_writings

# Convert PDFs to text
cd ../
python convert_to_text.py

# Alternative: Use the Jupyter notebook
jupyter notebook convert_to_text.ipynb
```

**Note**: Full scraping downloads ~2GB of PDFs. These can be safely deleted after text conversion.

## 🛠️ Advanced Usage

### Working with Dataset Versions

```python
# Initialize version control (creates v1 if needed)
from dataset_versioning import initialize_version_control
initialize_version_control()

# Get information about the latest version
from dataset_versioning import get_latest_version
latest = get_latest_version()
print(f"Latest version: {latest['version']} with {latest['num_entries']} entries")

# Convert specific version to Hugging Face format
from prepare_hf_dataset import convert_to_hf_dataset
dataset = convert_to_hf_dataset("v2")  # Specify any available version

# List all available versions
import os
versions = [d for d in os.listdir("./versions") if d.startswith("v")]
print(f"Available versions: {versions}")
```

### Data Structure

Each writing entry contains the following structured fields:

| Field | Description | Example |
|-------|-------------|---------|
| **text** | The full text content of the writing | "Bugün çok güzel bir gün..." |
| **course** | Course identifier | "Turkish 101", "Turkish 102" |
| **semester** | Academic semester information | "2016-2017 Fall" |
| **author** | Anonymized student identifier | "student_001" |
| **title** | Writing title (when available) | "Bir Sonbahar Günü" |
| **metadata** | Additional contextual information | JSON with course details |
| **url** | Original source URL (when available) | Original publication link |
| **file_id** | Internal file identifier | Hash-based unique ID |

**Data Quality Features:**
- Pre-processed and cleaned text content
- Consistent encoding (UTF-8)
- Structured metadata for easy filtering and analysis
- Deduplicated entries to ensure uniqueness

## 📈 Use Cases

This dataset is suitable for various research and applications:

### Natural Language Processing
- **Text Classification**: Genre classification, quality assessment, writing style analysis
- **Language Modeling**: Training Turkish language models, text generation systems
- **Sentiment Analysis**: Emotion detection in creative writing
- **Text Summarization**: Automatic summarization of student essays
- **Named Entity Recognition**: Turkish NER model training and evaluation

### Educational Research
- **Writing Quality Assessment**: Automated essay scoring systems
- **Language Learning Progression**: Analysis of student language development over time
- **Pedagogical Studies**: Writing instruction effectiveness research
- **Curriculum Development**: Evidence-based writing curriculum design

### Linguistic Studies
- **Turkish Language Corpus Analysis**: Large-scale linguistic pattern analysis
- **Stylistic Studies**: Computational stylistics and authorship attribution
- **Discourse Analysis**: Narrative structure and coherence studies
- **Morphological Analysis**: Turkish morphology in student writing

### Machine Learning & AI
- **Transfer Learning**: Pre-training for Turkish NLP models
- **Few-shot Learning**: Turkish text classification with limited data
- **Multilingual Models**: Cross-lingual transfer learning studies
- **Evaluation Benchmarks**: Turkish language model evaluation

### Digital Humanities
- **Comparative Literature Studies**: Computational analysis of Turkish creative writing
- **Cultural Analysis**: Social and cultural themes in student writing
- **Historical Linguistics**: Language change and variation studies
- **Digital Pedagogy**: Technology-enhanced writing instruction research

## 🤝 Contributing

We welcome contributions to improve the dataset and tools:

1. **Bug Reports**: Open an issue for any problems encountered
2. **Feature Requests**: Suggest improvements or new functionality
3. **Data Quality**: Report inconsistencies or errors in the dataset
4. **Documentation**: Help improve documentation and examples

### Development Setup

```bash
git clone https://github.com/selimfirat/bilkent-turkish-writings-dataset.git
cd bilkent-turkish-writings-dataset
pip install -r requirements.txt

# Check code formatting
black . --check
```

## 📊 Dataset Statistics

| Version | Entries | Size (CSV) | Content Period | Date Released | Status | Description |
|---------|---------|------------|----------------|---------------|---------|-------------|
| v1      | 6,844   | ~33MB      | 2014-2018      | 2018-02-03    | Stable  | Original dataset release |
| v2      | 9,119   | ~45MB      | 2014-2025 May  | 2025-05-24    | Latest  | Enhanced with additional content (+33%) |

### Content Distribution
- **Languages**: Turkish (primary), with some bilingual elements
- **Text Types**: Creative essays, narrative writing, descriptive pieces, argumentative texts
- **Quality**: Instructor-reviewed content with feedback on multiple dimensions

### Technical Validation
- **Encoding**: UTF-8 with proper Turkish character support (ı, ğ, ü, ş, ö, ç)
- **Deduplication**: Rigorous duplicate detection and removal process
- **Format Consistency**: Standardized CSV structure with validated schema
- **Content Filtering**: Removed incomplete or corrupted entries
- **Metadata Integrity**: All entries include complete metadata fields
- **Size Distribution**: Text lengths ranging from 100 to 5,000+ words
- **Quality Assurance**: Automated and manual validation processes applied

## ❓ Frequently Asked Questions

### Dataset Usage
**Q: Can I use this dataset for commercial purposes?**
A: No, this dataset is licensed for academic use only. Commercial use is prohibited.

**Q: How often is the dataset updated?**
A: The dataset is updated periodically as new content becomes available. Version 2.0 was released in May 2025 with significant additions.

**Q: What's the difference between versions?**
A: v1 contained 6,844 writings, while v2 includes 9,119 writings (33% increase). Each version is backward compatible.

### Technical Questions
**Q: What format is the dataset in?**
A: The primary format is CSV, but we also provide Hugging Face Datasets format and individual text files.

**Q: How do I handle Turkish character encoding?**
A: The dataset uses UTF-8 encoding. Use `pd.read_csv('texts.csv', encoding='utf-8')` in pandas.

**Q: Can I create my own train/test splits?**
A: Yes, use the provided `create_splits.py` script or the Hugging Face format which includes predefined splits.

### Research Questions
**Q: What type of research is this suitable for?**
A: NLP, educational research, linguistic analysis, machine learning, and digital humanities studies.

**Q: Are there any known limitations?**
A: The dataset reflects the writing styles and topics of Turkish university students from 2014-2025. Results may not generalize to other populations or time periods beyond this timeframe.

**Q: How should I cite this dataset?**
A: Use the provided BibTeX citation in the README or the CITATION.cff file for automated citation tools.

## 📝 Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{yilmaz_bilkent_turkish_writings_2025,
  title={Compilation of Bilkent Turkish Writings Dataset},
  author={Yilmaz, Selim F.},
  year={2025},
  publisher={Zenodo},
  doi={10.5281/zenodo.15498155},
  url={https://doi.org/10.5281/zenodo.15498155},
  version={2.0},
  note={Compilation of Turkish creative writings from Bilkent University Turkish 101 and 102 courses (2014-2025). 9,119 student writings collected and structured for NLP and educational research. Original content by Bilkent University students and instructors.}
}
```

**Alternative formats:**

*APA Style:*
```
Yilmaz, S. F. (2025). Compilation of Bilkent Turkish Writings Dataset [Data set]. Zenodo. https://doi.org/10.5281/zenodo.15498155
```

*Chicago Style:*
```
Yilmaz, Selim F. "Compilation of Bilkent Turkish Writings Dataset." Zenodo, 2025. https://doi.org/10.5281/zenodo.15498155.
```

## 📄 License

This dataset is released under an **Academic Use License**. This means:

**PERMITTED USES:**
- ✅ Academic research and education
- ✅ Non-commercial research projects
- ✅ Educational coursework and assignments
- ✅ Scientific publications and studies
- ✅ Personal learning and experimentation

**RESTRICTIONS:**
- ❌ Commercial use is prohibited
- ❌ Redistribution for profit is prohibited
- ❌ Use in commercial products or services is prohibited

**CONDITIONS:**
- **Attribution Required** — You must cite this dataset and the original sources
- **Academic Integrity** — Proper citation in all publications and research

See the [LICENSE](LICENSE) file for full details.

### Required Attribution

When using this dataset, please include:
```
Yilmaz, S. F. (2025). Compilation of Bilkent Turkish Writings Dataset. Zenodo. https://doi.org/10.5281/zenodo.15498155

Original source: Bilkent University Turkish Department
Source URL: https://stars.bilkent.edu.tr/turkce/
GitHub Repository: https://github.com/selimfirat/bilkent-turkish-writings-dataset
```

## 🙏 Acknowledgments

- **Original Content Creators**: Students and instructors of Turkish 101 and 102 courses at Bilkent University (2014-2025)
- **Bilkent University Turkish Department** for creating and publishing the original writings
- **Bilkent University** for supporting open educational resources and public access
- **Dataset Compiler**: Selim F. Yilmaz for collecting, processing, structuring, and distributing the dataset

**Important**: This dataset is a compilation of existing publicly available content. The original creative works were authored by Bilkent University students and instructors. The contribution of this project lies in the systematic collection, processing, and structuring of this content for research purposes.

## 📞 Contact

For questions, issues, or collaborations:
- Open an issue on [GitHub](https://github.com/selimfirat/bilkent-turkish-writings-dataset/issues)
- Visit the original source: [Bilkent Turkish Writings](https://stars.bilkent.edu.tr/turkce/)

## 🔗 Related Resources

- [Zenodo Dataset DOI](https://doi.org/10.5281/zenodo.15498155)
- [Bilkent University](https://www.bilkent.edu.tr/)
- [Turkish Language Resources](https://stars.bilkent.edu.tr/turkce/)
- [Hugging Face Datasets Documentation](https://huggingface.co/docs/datasets/)
- [Scrapy Documentation](https://docs.scrapy.org/)

---

**Last Updated**: May 2025  
**Dataset Version**: v2 (Latest)  
**Maintainer**: Selim F. Yilmaz (@selimfirat)

## 🛡️ Data Ethics & Responsible Use

### Ethical Considerations
- **Content Origin**: All writings were originally created by Bilkent University students and instructors
- **Public Availability**: Only publicly available content was collected and compiled
- **Permission Respect**: Original publication permissions and terms respected
- **Academic Integrity**: Dataset designed for legitimate academic and research purposes
- **Cultural Sensitivity**: Respectful use of Turkish language and cultural content expected
- **Attribution**: Clear attribution to both original creators and dataset compiler

### Data Collection Ethics
- **Transparent Methodology**: Open-source scraping and processing tools provided
- **No Private Data**: No access to restricted or private university systems
- **Respect for Source**: Maintains links and attribution to original publication source
- **Version Control**: Clear documentation of collection and processing steps

### Responsible Use Guidelines
- **Attribution Required**: Always cite the dataset and original source
- **Academic Purpose**: Use only for non-commercial research and education
- **Respect Content**: Maintain dignity and respect for student work
- **Quality Research**: Use appropriate methodologies and report limitations
- **Community Benefit**: Share insights that benefit the research community

### Data Protection
- **No Re-identification**: Do not attempt to identify individual students
- **Secure Storage**: Store dataset securely and limit access as appropriate
- **Version Control**: Use official versions and track data provenance
- **Reporting Issues**: Report any ethical concerns or data quality issues

## 🔍 Data Provenance & Collection

### Original Source
The writings in this dataset were originally created by students enrolled in Turkish 101 and Turkish 102 courses at Bilkent University between 2014-2025. These courses focus on developing creative writing skills in Turkish through active learning methodologies.

### Collection Process
1. **Source Identification**: Writings were collected from the publicly available Bilkent University Turkish Department website (https://stars.bilkent.edu.tr/turkce/)
2. **Systematic Scraping**: Automated collection using custom web scraping tools (included in this repository)
3. **Content Processing**: PDF documents were converted to structured text format
4. **Data Cleaning**: Removal of duplicates, formatting artifacts, and incomplete entries
5. **Metadata Enhancement**: Addition of structured metadata for research use
6. **Quality Validation**: Manual and automated validation of content integrity

### Data Transformation Pipeline
- **Format Conversion**: PDF → Text → Structured CSV
- **Encoding Standardization**: UTF-8 encoding for proper Turkish character support
- **Metadata Extraction**: Course information, semester data, and other publicly available details
- **Deduplication**: Hash-based duplicate detection and removal
- **Schema Validation**: Consistent field structure across all entries

### Ethical Considerations
- All collected content was already publicly available
- No private or restricted materials were accessed
