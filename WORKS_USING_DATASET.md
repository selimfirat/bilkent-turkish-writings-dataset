# Works Using the Bilkent Turkish Writings Dataset

This document lists academic papers, publications, and research works that have used the Bilkent Turkish Writings Dataset in their research.

## Academic Papers and Publications

### 1. TURNA: A Turkish Encoder-Decoder Language Model for Enhanced Understanding and Generation (2024)

- **Authors**: Gökçe Uludoğan, Zeynep Yirmibeşoğlu Balal, Furkan Akkurt, Melikşah Türker, Onur Güngör, Susan Üsküdarlı
- **Publication**: arXiv:2401.14373
- **DOI**: https://doi.org/10.48550/arXiv.2401.14373
- **Link**: https://arxiv.org/abs/2401.14373
- **Use Case**: Used the dataset as part of their diverse corpus for training the TURNA language model, which is specifically designed for Turkish language understanding and generation tasks. TURNA is an encoder-decoder architecture based on the unified framework UL2.
- **Research Area**: Language Model Training, Turkish NLP

### 2. Evaluating Morphological Compositional Generalization in Large Language Models (2024)

- **Authors**: Mete Ismayilzada, Defne Circi, Jonne Sälevä, Hale Sirin, Abdullatif Köksal, Bhuwan Dhingra, Antoine Bosselut, Duygu Ataman
- **Publication**: arXiv:2410.12656 (Accepted to NAACL 2025)
- **DOI**: https://doi.org/10.48550/arXiv.2410.12656
- **Link**: https://arxiv.org/abs/2410.12656
- **Use Case**: Specifically used "the Bilkent Turkish Writings Dataset as our base corpus which contains 6,844 creative writings of Turkish 101 and Turkish 102 courses" for evaluating morphological compositional generalization in large language models, focusing on agglutinative languages like Turkish and Finnish.
- **Research Area**: Morphological Analysis, Compositional Generalization, LLM Evaluation

### 3. Automatic Lexical Simplification for Turkish (2022)

- **Authors**: Ahmet Yavuz Uluslu
- **Publication**: arXiv:2201.05878
- **DOI**: https://doi.org/10.48550/arXiv.2201.05878
- **Link**: https://arxiv.org/abs/2201.05878
- **Use Case**: Used "1000 complex sentences from the Bilkent Creative Writing dataset" for developing and testing the first automatic lexical simplification system for Turkish. The dataset provided complex sentence examples for word-level simplification tasks.
- **Research Area**: Text Simplification, Lexical Simplification, Turkish NLP

### 4. Bella Turca: A Large-Scale Dataset of Diverse Text Sources for Turkish Language Modeling (2024)

- **Authors**: Duygu Altinok
- **Publication**: Text, Speech, and Dialogue (TSD 2024), Lecture Notes in Computer Science, vol 15048
- **DOI**: https://doi.org/10.1007/978-3-031-70563-2_16
- **Link**: https://link.springer.com/chapter/10.1007/978-3-031-70563-2_16
- **Use Case**: References the Bilkent Turkish writings dataset (https://stars.bilkent.edu.tr/turkce/) as one of the diverse text sources included in the comprehensive Bella Turca corpus (265GB) for Turkish language modeling. The dataset is mentioned in footnote 4 of the paper.
- **Research Area**: Language Model Training, Corpus Creation, Turkish NLP

### 5. VNLP: Turkish NLP Package (2024)

- **Authors**: Meliksah Turker, Mehmet Erdi Ari, Aydin Han
- **Publication**: arXiv:2403.01309
- **DOI**: https://doi.org/10.48550/arXiv.2403.01309
- **Link**: https://arxiv.org/abs/2403.01309
- **Use Case**: Likely used the dataset for training or evaluation of their comprehensive Turkish NLP package, which includes tools for sentiment analysis, named entity recognition, morphological analysis, and part-of-speech tagging.
- **Research Area**: NLP Tool Development, Turkish Language Processing

### 6. Same Sentence Prediction: A new Pre-training Task for BERT (2021)

- **Authors**: K. Sonmezoz, M. F. Amasyali
- **Publication**: 2021 Innovations in Intelligent Systems and Applications Conference (ASYU), Elazig, Turkey
- **DOI**: https://doi.org/10.1109/ASYU52992.2021.9598954
- **Link**: https://ieeexplore.ieee.org/abstract/document/9598954
- **Use Case**: Used as part of the Turkish text corpus for evaluating the proposed "Same Sentence Prediction" pre-training task for BERT models. The paper presents a novel pre-training objective where the model learns to predict whether two sentences are the same, which helps improve Turkish language understanding capabilities.
- **Research Area**: Pre-training Tasks, BERT, Turkish NLP, Self-Supervised Learning
- **Note**: *For detailed methodology and specific usage statistics, please refer to the original paper or contact the authors directly.*

### 7. Finding the Relationship Between News and Social Media Users' Emotions in the COVID-19 Process (2020)

- **Authors**: Ahmet Anıl Müngen, İrfan Aygün, Mehmet Kaya
- **Publication**: Sakarya University Journal of Computer and Information Sciences, vol. 3, no. 3, pp. 250-263
- **DOI**: https://doi.org/10.35377/saucis.03.03.830867
- **Link**: http://saucis.sakarya.edu.tr/en/download/article-file/1413664
- **Use Case**: Used as part of a combined Turkish text corpus (along with the TREMO dataset) to create word vectors for LSTM-based sentiment analysis. The dataset contributed to forming word embeddings that improved semantic understanding in the analysis of COVID-19 related social media emotions and user reactions.
- **Research Area**: Sentiment Analysis, Word Embeddings, Social Media Analysis, Turkish NLP

### 8. Derlem Dil Bilim ve Edebiyat Çalışmalarının Kesişim Noktası: Derlem Biçem Bilimi (2021)

- **Authors**: Şahru Pilten Ufuk
- **Publication**: ResearchGate publication (2021)
- **DOI**: [To be confirmed]
- **Link**: https://www.researchgate.net/publication/357539519_Derlem_Dil_Bilim_ve_Edebiyat_Calismalarinin_Kesisim_Noktasi_Derlem_Bicem_Bilimi
- **Use Case**: [Subject to verification] - Research work on corpus stylistics and the intersection of corpus linguistics with literary studies. May utilize Turkish text corpora including the Bilkent Turkish Writings Dataset for stylistic analysis of Turkish texts.
- **Research Area**: Corpus Stylistics, Turkish Linguistics, Computational Stylistics, Literary Corpus Analysis
- **Note**: *This entry requires verification of actual dataset usage. The publication focuses on corpus stylistics methodology in Turkish literary studies.*

## Dataset Usage Statistics

- **Monthly Downloads**: 30+ downloads (HuggingFace)
- **Total Dataset Size**: 76.5 MB
- **Current Version**: v2 with 9,119 writings
- **Previous Version**: v1 with 6,844 writings
- **Available Formats**: Parquet, CSV, HuggingFace Datasets
- **License**: Academic Use Only
- **DOI**: 10.5281/zenodo.15498155
- **HuggingFace**: https://huggingface.co/datasets/selimfirat/bilkent-turkish-writings-dataset

## Research Areas Where the Dataset is Used

1. **Language Model Training**: Used as training corpus for Turkish language models
2. **Morphological Analysis**: Evaluating how well models handle Turkish morphology and agglutination
3. **Text Simplification**: Developing lexical simplification systems for Turkish using complex sentence examples
4. **Natural Language Processing Tools**: Development of Turkish-specific NLP packages and libraries
5. **Compositional Generalization**: Testing language models' ability to understand morphological composition
6. **Corpus Creation**: Contributing to large-scale diverse datasets for Turkish language modeling
7. **Creative Writing Analysis**: Studying Turkish creative writing patterns and linguistics
8. **Educational Assessment**: Potential use in automated writing evaluation systems
9. **Corpus Stylistics**: Computational analysis of stylistic patterns and linguistic features in Turkish texts

## Citation Impact Analysis

- **Growth Trend**: Increasing usage in Turkish NLP research community across multiple years (2022-2025)
- **Research Impact**: Establishing itself as a standard resource for Turkish language processing research
- **International Recognition**: Used in papers accepted to major conferences (NAACL 2025, TSD 2024)
- **Diverse Applications**: From text simplification to large-scale corpus creation

## Potential Future Applications

Based on current research trends and the dataset's characteristics:

- Turkish text generation models
- Educational writing assessment tools
- Corpus linguistics studies
- Sentiment analysis in Turkish creative writing
- Style transfer research for Turkish
- Creative writing AI systems
- Turkish language learning applications
- Automated essay scoring systems
- Linguistic pattern analysis
- Cross-lingual creative writing studies

## Citation Information

If you use this compilation in your research, please cite the original dataset:

```bibtex
@dataset{yilmaz_bilkent_turkish_writings_2025,
  title={Compilation of Bilkent Turkish Writings Dataset},
  author={Yilmaz, Selim F.},
  year={2025},
  publisher={Zenodo},
  doi={10.5281/zenodo.15498155},
  url={https://doi.org/10.5281/zenodo.15498155},
  version={v2},
  note={Compilation of Turkish creative writings from Bilkent University Turkish 101 and 102 courses (2014-2025). Original content by Bilkent University students and instructors.}
}
```

## How to Report New Uses

If you have used this dataset in your research or know of additional works that should be listed here, please:

1. Open an issue on the [GitHub repository](https://github.com/selimfirat/bilkent-turkish-writings-dataset)
2. Provide the following information:
   - Paper title and authors
   - Publication venue and date
   - DOI or link to the paper
   - Brief description of how the dataset was used

---

*Last updated: May 26, 2025*

*This list is maintained as part of the Bilkent Turkish Writings Dataset project to track its impact and usage in the research community.*
