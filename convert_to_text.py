
#!/usr/bin/env python
# coding: utf-8

"""
Convert PDFs to text for the Bilkent Turkish Writings Dataset.
"""

import pdfplumber  # You may need to install this: pip install pdfplumber
import glob
import pandas as pd  # You may need to install this: pip install pandas
import pathlib
import os


# __Note:__ The parts below are seperated since the first step takes to much time and to be able to continue when terminated.
# Simply, for continuos processing of PDFs.

# In[3]:


# Converting PDFs and append them to texts array
path = "./data/full/"
texts_path = "./data/texts/"

print(f"Looking for files in: {path}")
pathlib.Path(texts_path).mkdir(parents=True, exist_ok=True) 
files = glob.glob(path + "*")
print(f"Found {len(files)} files to process")

if len(files) == 0:
    print("No files found! Check if the data/full directory exists and contains files.")
    exit(1)

processed_count = 0
skipped_count = 0

for f in files:
    f_name = os.path.basename(f)  # Use os.path.basename for cross-platform compatibility
    txt_path = texts_path + f_name + ".txt"
    
    file_path = pathlib.Path(txt_path)
    
    if file_path.exists():
        print(f"Skipping existing file: {f_name}")
        skipped_count += 1
        continue

    # Check if file is readable and has some content
    try:
        with open(f, 'rb') as test_file:
            header = test_file.read(8)
            if not header.startswith(b'%PDF'):
                print(f"Skipping non-PDF file: {f_name}")
                skipped_count += 1
                continue
    except Exception as e:
        print(f"Error reading file {f_name}: {e}")
        skipped_count += 1
        continue

    print(f"Processing: {f_name}")
    try:
        pdf = pdfplumber.open(f)
    except Exception as e:
        print(f"Error opening PDF file {f}: {e}")
        print(f"Skipping corrupted file: {f_name}")
        skipped_count += 1
        continue
        
    text = u''
    try:
        for page in pdf.pages:
            try: # since pdfplumber tries to convert "P14" into decimal for some reason
                et = page.extract_text()
            except Exception as e:
                print(f"Error extracting text from page in {f_name}: {e}")
                et = None
            
            if et is not None: # since pdfplumber returns None when an empty page occurs
                text += et
            else:
                print("Extracted text is None in file " + f)
    finally:
        pdf.close()  # Close the PDF file properly

    file = open(txt_path, "wb")
    file.write(text.encode("utf-8", "ignore"))
    file.close()
    processed_count += 1
    
    if processed_count % 100 == 0:
        print(f"Processed {processed_count} files so far...")

print(f"PDF processing complete! Processed: {processed_count}, Skipped: {skipped_count}")
print(f"Total text files created: {len(glob.glob(texts_path + '*'))}")


# In[15]:


# read texts
print("Reading extracted text files...")
texts_path = "./data/texts/"
text_files = glob.glob(texts_path + "*")
print(f"Found {len(text_files)} text files to read")

texts = []
for i, f in enumerate(text_files):
    try:
        with open(f, 'rb') as file:
            texts.append(file.read().decode("utf-8"))
    except Exception as e:
        print(f"Error reading text file {f}: {e}")
        texts.append("")  # Add empty string to maintain index consistency
    
    if (i + 1) % 1000 == 0:
        print(f"Read {i + 1} text files...")
        
# Create pandas dataframe for texts
print("Creating DataFrame...")
df = pd.DataFrame({ "text": pd.Series(texts) })
print(f"DataFrame created with {len(df)} entries")
df.head()


# In[16]:


# Number of writings
df.shape


# In[17]:


# Convert dataframe to csv
print(f"Converting {len(df)} texts to CSV...")
df.to_csv("data/texts.csv", index=False, encoding='utf-8', escapechar='\\', quoting=1)
print("Successfully saved to data/texts.csv")

