# Bilkent Turkish Writings Dataset

This dataset contains the turkish creative writings of Turkish 101 and Turkish 102 courses between 2014-2018. It contains 4 publicly published writings of students 2 for each course.
The writings in this dataset promotes creativity, content, composition, grammar, spelling and punctuation.

The writings can be found [here](https://stars.bilkent.edu.tr/turkce/) as bunch of PDFs.

The dataset is continuously growing since each semester new texts are published publicly.

Currently, there are __6,844 writings__ in this dataset which is 33.1MB of data in a csv file.

## Description of Turkish 101 & 102 in Bilkent University

This course is the first of a sequence of two courses designed to develop creative writing skills of the students through their own writings in Turkish. It is an active learning course. Students write their own blogs and instructors comment and send feedback about the creativity, content, composition, grammar, spelling and punctuation of the writing regularly.

## Downloading the dataset

The data can be found in [./data/texts.csv](./data/texts.csv).

```
git clone https://github.com/selimfirat/bilkent-turkish-writings-dataset.git
mv ./bilkent-turkish-writings-dataset/data/texts.csv <TARGET_PATH>
```

## How to scrape from scratch
```
git clone https://github.com/selimfirat/bilkent-turkish-writings-dataset.git
pip install -r requirements.txt
cd bilkent-turkish-writings-dataset/scraper
scrapy crawl bilkent_turkish_writings
cd ../
python convert_to_text.py
```

In the end, there will be ~2GB of PDFs(it worth to continuous crawling & preprocessing) which can be deleted after the converting to text is done.
The last two line suggested to executed using [this notebook](./convert_to_text.ipynb).
