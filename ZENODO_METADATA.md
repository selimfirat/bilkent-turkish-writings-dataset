# Zenodo Metadata for Compilation of Bilkent Turkish Writings Dataset

## Required Metadata for Zenodo Upload

### Basic Information
- **Title**: Compilation of Bilkent Turkish Writings Dataset
- **Description**: A comprehensive compilation of Turkish creative writings from Bilkent University's Turkish 101 and Turkish 102 courses (2014-2025). This dataset contains 9,119 student writings originally created by Bilkent University students and instructors, focusing on creativity, content, composition, grammar, spelling, and punctuation development. The writings were originally published publicly by Bilkent University and have been systematically collected, processed, and structured into a research dataset. Version 2.0 includes significant expansion with 33% more content compared to the initial release, making it one of the largest publicly available Turkish creative writing corpora for academic research. Note: This is a compilation of existing publicly available content - the original creative works were authored by Bilkent University students and instructors.

### Dataset Compiler/Creator
- **Name**: Selim F. Yilmaz (Dataset Compilation & Processing)
- **Role**: Data collection, processing, and structuring
- **ORCID**: [https://orcid.org/0000-0002-0486-7731](https://orcid.org/0000-0002-0486-7731)

### Original Content Creators & Contributors
- **Bilkent University Turkish Department** (Original Content Publisher)
- **Students and Instructors** of Turkish 101 and 102 courses (Original Content Authors, 2014-2025)
- **Bilkent University** (Institutional Support)

### License
- **License**: Academic Use Only (Non-commercial research and education)

### Keywords/Subjects
- Turkish language
- Creative writing
- Educational dataset
- Natural language processing
- Corpus linguistics
- Language learning
- Text analysis
- Academic writing
- Student writing
- Turkish corpus
- Machine learning
- Digital humanities
- Educational technology
- Text mining
- Computational linguistics
- Language education
- Writing assessment

### Resource Type
- **Type**: Dataset

### Version
- **Version**: 2.0
- **Publication Date**: 2025-05-24

### Related Identifiers
- **GitHub Repository**: https://github.com/selimfirat/bilkent-turkish-writings-dataset
- **Original Source**: https://stars.bilkent.edu.tr/turkce/
- **Hugging Face**: https://huggingface.co/datasets/selimfirat/bilkent-turkish-writings-dataset (if applicable)

### References
- Original source: Bilkent University Turkish Department writings collection
- Course information: Turkish 101 and Turkish 102 creative writing courses

### Notes
- Dataset contains publicly available student writings
- Data has been processed and structured for research use
- Contains both metadata and full text content
- Suitable for NLP, educational research, and linguistic analysis
- Version 2.0 represents a 33% increase from original dataset
- Text encoding: UTF-8 for proper Turkish character support
- Quality assured through deduplication and content validation
- Includes comprehensive metadata for advanced filtering and analysis
- Regular version updates planned as new content becomes available

## Responsible Data Sharing Statement

This dataset represents a compilation of publicly available educational content. The collection and distribution process follows these principles:

### Content Attribution
- **Original Authors**: Bilkent University students and instructors (2014-2025)
- **Original Publisher**: Bilkent University Turkish Department
- **Dataset Compiler**: Selim F. Yilmaz (collection, processing, structuring)
- **Compilation Purpose**: Academic research and educational use

### Ethical Compliance
- All content was already publicly available at time of collection
- No private or restricted materials were accessed
- Student privacy protected through anonymization
- Original publication terms and permissions respected
- Academic use license ensures appropriate usage

### Quality Assurance
- Systematic collection methodology documented
- Open-source tools provided for transparency
- Version control for reproducibility
- Community feedback mechanisms established

This compilation serves the academic community while respecting the rights and contributions of all original content creators.

## Files to Include in Zenodo Upload
1. **texts.csv** - Main dataset file (~45MB, 9,119 entries)
2. **README.md** - Comprehensive documentation and usage guide
3. **LICENSE** - Academic Use License terms
4. **CITATION.cff** - Machine-readable citation information
5. **requirements.txt** - Python dependencies for dataset tools
6. **dataset_versioning.py** - Version management utilities
7. **prepare_hf_dataset.py** - Hugging Face dataset conversion script
8. **update_dataset.py** - Dataset update and maintenance script
9. **create_splits.py** - Train/validation/test split creation
10. **convert_to_text.py** - PDF to text conversion utilities

## Technical Specifications
- **File Format**: CSV with UTF-8 encoding
- **Total Size**: ~45MB
- **Entries**: 9,119 individual writings
- **Fields**: 8 structured columns per entry
- **Compatibility**: Python 3.7+, pandas, datasets library
- **Validation**: Schema validated and quality checked

## Recommended Communities on Zenodo
- **Natural Language Processing** - Primary community for NLP research
- **Digital Humanities** - For computational humanities research
- **Educational Technology** - For educational data and tools
- **Turkish Studies** - For Turkish language and literature research
- **Corpus Linguistics** - For linguistic corpus research
- **Machine Learning** - For ML/AI applications
- **Open Educational Resources** - For educational content sharing
