#do not have to run this file again
#created the 'textbyyear.txt' file, with 17 strings of yearly text (1 per year)

import re
import requests
from bs4 import BeautifulSoup
from getdates import *
from compiledata import *

#function to webscrape a link, arg is one link (cleaned)
def webscrape_link(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    text_string = ""
    for info in soup.find_all("p"):
        text_string = text_string + " " + info.get_text()

    text_string = re.sub("\n", " ", text_string)
    text_string = re.sub("\s+", " ", text_string)

    return text_string

#get all the links, group by year, clean them
links = get_links_and_dates()[0]
grouped_links = group_links_by_year(links)
cleaned_grouped_links = [[link.strip('\n') for link in year] for year in grouped_links]

#create a list to join all text per year
yearly_text = []
for year in cleaned_grouped_links:
    year_text = ' '.join(webscrape_link(str(link)) for link in year)
    yearly_text.append(year_text)

#write to a file
with open('textbyyear.txt', 'w') as file:
   for element in yearly_text:
        file.write(str(element) + '\n')
