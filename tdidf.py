from bs4 import BeautifulSoup
import re
import glob
import os
import requests
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from pathlib import Path
import pandas as pd
import glob

def webscrape_link(file):
    text_list = []
    page = file.read()
    soup = BeautifulSoup(page, "html.parser")
    text_string = ""
    for info in soup.find_all("p"):
        text_string = text_string + " " + info.get_text()
    text_string = re.sub("\n", " ", text_string)
    text_string = re.sub("\s+", " ", text_string)
    text_list.append(text_string)  
    return text_list

'''
links = []
with open('data/links.txt', 'r') as file:
    for line in file:
        links.append(line.strip())

for link in links:
    page = requests.get(link)
    newsoup = BeautifulSoup(page.content, "html.parser")

    mystring = ""
    for info in newsoup.find_all("p"):
        mystring = mystring + " " + info.get_text()

    mystring = re.sub("\n", " ", mystring)
    mystring = re.sub("\s+", " ", mystring)
    mystring = re.sub("\[.*?\]", " ", mystring)

    cleanedlink = re.sub('/', '', link)
    filename = cleanedlink + '.txt'

    with open('txtfiles/' + filename, 'w') as file:
        file.write(mystring)
'''

text_files = glob.glob('txtfiles/*.txt')
file_names = [Path(text).stem for text in text_files]

tfidf_vectorizer = TfidfVectorizer(input='filename', stop_words='english')
tfidf_vector = tfidf_vectorizer.fit_transform(text_files)

tfidf_df = pd.DataFrame(tfidf_vector.toarray(), index=file_names, columns=tfidf_vectorizer.get_feature_names_out())
tfidf_df.stack().reset_index()
tfidf_df = tfidf_df.stack().reset_index()
tfidf_df = tfidf_df.rename(columns={0:'tfidf', 'level_0': 'document','level_1': 'term', 'level_2': 'term'})
tfidf_df.sort_values(by=['document','tfidf'], ascending=[True,False]).groupby(['document']).head(10)