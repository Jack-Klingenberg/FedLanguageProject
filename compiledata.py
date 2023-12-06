# Authors: Ben Elenbaas, Jack Klingenberg
# Description: Create a csv file for all the text from our meetings. Each element is the text from a particular meeting along with the date of the meeting.

from bs4 import BeautifulSoup
import glob
import pandas as pd
import re 
import sys

#webscrape a meeting, perform regex replacements, append to a list
def text_webscrape(file):
    text_list = []

    # Read file from path argument and create BeautifulSoup 
    page = file.read()
    soup = BeautifulSoup(page, "html.parser")

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

def main():
    matrix = []

    for path in glob.glob("./data/html/*"):
        with open(path,"r") as file:
            date = path.split("/minutes")[-1].split(".")[0]
            year = date[0:4]
            month = date[4:6]
            day=date[6:8]

            text = text_webscrape(file) 

            row = [year,month,day,text]
            matrix.append(row)
    
    df = pd.DataFrame(matrix).sort_values(by=[0,1,2])
    df.columns = ["year", "month", "day", "text"]

    try:
        df.to_csv(sys.argv[1], index=False)
    except:
        print("Not saving dataset...")
        return

if __name__ == "__main__":
    main()
    



