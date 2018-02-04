
# coding: utf-8

# In[ ]:


# Imports
import pdfplumber
import glob
import pandas as pd
import pathlib


# __Note:__ The parts below are seperated since the first step takes to much time and to be able to continue when terminated.
# Simply, for continuos processing of PDFs.

# In[3]:


# Converting PDFs and append them to texts array
path = "./data/full/"
texts_path = "./data/texts/"

pathlib.Path(texts_path).mkdir(parents=True, exist_ok=True) 
files = glob.glob(path + "*")

for f in files:
    f_name = f.split("\\")[-1]
    txt_path = texts_path + f_name + ".txt"
    
    file_path = pathlib.Path(txt_path)
    
    if file_path.exists():
        continue

    pdf = pdfplumber.open(f)
    text = u''
    for page in pdf.pages:
        try: # since pdfplumber tries to convert "P14" into decimal for some reason
            et = page.extract_text()
        except:
            pass
        
        if et is not None: # since pdfplumber returns None when an empty page occurs
            text += et
        else:
            print("Extracted text is None in file " + f)

    file = open(txt_path, "wb")
    file.write(text.encode("utf-8", "ignore"))
    file.close()
    


# In[15]:


# read texts
texts_path = "./data/texts/"
text_files = glob.glob(texts_path + "*")
texts = []
for f in text_files:
    with open(f, 'rb') as file:
        texts.append(file.read().decode("utf-8"))
        
# Create pandas dataframe for texts
df = pd.DataFrame({ "text": pd.Series(texts) })
df.head()


# In[16]:


# Number of writings
df.shape


# In[17]:


# Convert dataframe to csv
df.to_csv("data/texts.csv")

