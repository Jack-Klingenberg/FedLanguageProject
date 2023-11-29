import sys
import csv
import re
import nltk
from nltk.corpus import stopwords
from getdates import *
from compiledata import *
import glob
import requests
from nltk.stem import WordNetLemmatizer
from nltk.collocations import *

'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from pathlib import Path
import pandas as pd
'''

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
stoplist.extend([".", ",", "?", "could", "would", "“", "”", "’", ";", "!", 's', 'meeting', 'markets', 'financial', 'participants', 'prices', 'economic', 'conditions', 'committee', 'core', 'outlook', 'housing', "'s", 'spending', 'committee', 'remained', 'rate', 'likely', 'also', 'expected', 'consumer', 'quarter', 'data', 'market', 'generally', 'higher', 'period', 'price', 'generally', 'committee', 'june', "''", 'continued', 'progress', 'economy', 'bank', 'reserve', 'june', 'committee\\', 'reserve', ')', 'board', 'division', 'federal', '``', '2', 'goals', 'monetary', 'supply', 'policy', 'u.s.', '(', 'noted', '2022', 'balance', 'percent', 'range', 'treasury', 'activity', 'stance', 'intermeeting', 'recent', 'year', 'time', 'businesses', 'governors', 'appropriate', 'operations', 'support', 'agreed', 'members', '2020', 'director', 'term', 'staff', 'months', '&', 'united', 'states', 'new', 'york', 'achilles', 'sangster', 'annette', 'samuel', 'min', 'michele', 'sylvain', '2-', '5-', 'seth', 'boards', 'met', 'wright', 'met', 'national', 'glenn', 'weekend', 'andrea', 'laura', 'naureen', '737', 'andrew', 'marc', 'ron', 'sally', '1-1/2', '10-', 'ivan'])

#most common tokens
'''
print('\n')
tokens_2020 = [w for w in tokenized_list[13] if w.lower() not in stoplist]
fdist2020 = nltk.FreqDist(tokens_2020)
print(fdist2020.most_common(20))

print('\n')
tokens_2022 = [w for w in tokenized_list[15] if w.lower() not in stoplist]
fdist2022 = nltk.FreqDist(tokens_2022)
print(fdist2022.most_common(20))
'''

#bigrams
'''
print('\n')
bigrams2022 = nltk.ngrams(tokenized_list[15], 2)
bigramlist2022 = list(bigrams2022)
bigramfreq2022 = nltk.FreqDist(bigramlist2022)
#print(bigramfreq2022.most_common(10))

print('\n')
for b in bigramfreq2022.most_common(1000):
    if b[0][0].lower() not in stoplist and b[0][1].lower() not in stoplist:
        print(b)
'''

#collocations
#have to remove names
'''
tokens_2020_nostops = [w for w in tokenized_list[13] if w.lower() not in stoplist]

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder2020 = BigramCollocationFinder.from_words(tokens_2020_nostops)
finder2020.apply_freq_filter(3)
for w in finder2020.nbest(bigram_measures.pmi, 10):
    print(" ".join(w))
'''