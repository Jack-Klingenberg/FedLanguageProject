#webscrape the html files for text. takes a list of urls as an arg

import requests
from bs4 import BeautifulSoup
import re

def text_webscrape(links):

    #list to store strings of text, one element for each webpage
    text_list = []

    for url in links:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        #retrieve all of the text for current url, change into a string of text
        text_string = ""
        for info in soup.find_all("p"):
            text_string = text_string + " " + info.get_text()

        #replace each newline character with a space
        #replace 1+ consecutive whitespace characters (spaces, tabs, newlines) with a single space
        text_string = re.sub("\n", " ", text_string)
        text_string = re.sub("\s+", " ", text_string)

        text_list.append(text_string)  

    return text_list


