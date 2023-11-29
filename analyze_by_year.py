import sys
import csv
import re
import nltk
from nltk.corpus import stopwords
from getdates import *
from compiledata import *
import glob
import requests

#text_list is a list of all the text, with one element per file
def read_in_data():
    with open('textbyyear.txt', 'r') as file:
        lines = file.readlines()
    return lines
text_list = read_in_data()

#tokenize the text_list
tokenized_list = []
for text in text_list:
    tokenized_text = nltk.word_tokenize(text)
    tokenized_list.append(tokenized_text)

#stop words
stoplist = stopwords.words("english")
stoplist.extend([".", ",", "?", "could", "would", "“", "”", "’", ";", "!", 's', 'meeting', 'markets', 'financial', 'participants', 'prices', 'economic', 'conditions', 'committee', 'core', 'outlook', 'housing', "'s", 'spending', 'committee', 'remained', 'rate', 'likely', 'also', 'expected', 'consumer', 'quarter', 'data', 'market', 'generally', 'higher', 'period', 'price', 'generally', 'committee', 'june', "''", 'continued', 'progress', 'economy', 'bank', 'reserve', 'june', 'committee\\', 'reserve', ')', 'board', 'division', 'federal', '``', '2', 'goals', 'monetary', 'supply', 'policy', 'u.s.', '(', 'noted', '2022', 'balance', 'percent', 'range', 'treasury'])

#testing
tokens_2020 = [w for w in tokenized_list[13] if w.lower() not in stoplist]
fdist2020 = nltk.FreqDist(tokens_2020)
print(fdist2020.most_common(20))

print('\n')

tokens_2022 = [w for w in tokenized_list[15] if w.lower() not in stoplist]
fdist2022 = nltk.FreqDist(tokens_2022)
print(fdist2022.most_common(20))
