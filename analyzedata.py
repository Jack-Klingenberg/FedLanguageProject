import sys
import csv
import re
import nltk
from nltk.corpus import stopwords
from getdates import *
from compiledata import *


def read_in_data():
    lines = []
    with open('data/ds1.csv', 'r') as csv_file:
        for line in csv_file:
            lines.append(line.strip())
    return lines

text_list = read_in_data()

tokenized_list = []
for text in text_list:
    tokenized_text = nltk.word_tokenize(text)
    tokenized_list.append(tokenized_text)

token_count = 0
type_count = 0
for token_list in tokenized_list:
    token_count += len(token_list)
    type_count += len(set(token_list))

stoplist = stopwords.words("english")
stoplist.extend([".", ",", "?", "could", "would", "“", "”", "’", ";", "!", 's', 'meeting', 'markets', 'financial', 'participants', 'prices', 'economic', 'conditions', 'committee', 'core', 'outlook', 'housing', "'s", 'spending', 'committee', 'remained', 'rate', 'likely', 'also', 'expected', 'consumer', 'quarter', 'data', 'market', 'generally', 'higher', 'period', 'price', 'generally', 'committee', 'june', "''", 'continued', 'progress', 'economy', 'bank', 'reserve', 'june', 'committee\\', 'reserve', ')', 'board', 'division', 'federal', '``', '2', 'goals', 'monetary', 'supply', 'policy'])

#print(stoplist)

#fdist = nltk.FreqDist(tokenized_list[0])
#x = fdist.most_common(20)
#print(x)

d = [w for w in tokenized_list[1] if w.lower() not in stoplist]
fdisty = nltk.FreqDist(d)
y = fdisty.most_common(20)
print(y)

#print(stoplist)

print('\n')

g = [w for w in tokenized_list[111] if w.lower() not in stoplist]
fdistz = nltk.FreqDist(g)
z = fdistz.most_common(20)
print(z)


#'lines' is a list of string of all the text per html file
#can now tokenize

'''
links = get_links_and_dates()[0]
grouped_links = group_links_by_year(links)

for year_links in grouped_links:
    for link in year_links:
        link_text = text_webscrape(link)
'''