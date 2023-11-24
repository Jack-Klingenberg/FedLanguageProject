# Author: Jack Klingenberg
# Date: Nov 22, 2023
# Description: Python script to gather all links to FOMC minute html files without direct web scraping. Uses Requests library to test if link is link is valid
# and if it is adds it to argv[3] file. Checks for minutes between Jan 1, argv[1] and Dec 31, year argv[2]

import requests
import sys 
from tqdm import tqdm

START = int(sys.argv[1])
END  = int(sys.argv[2])
TARGET = sys.argv[3]
def check_link_exists(url):
    try:
        response = requests.head(url)
        return response.status_code // 100 == 2
    except requests.RequestException:
        return False

links = []
print("Links processing...")
progressbar = tqdm(total=(END-START+1)*12*31)
for year in range(START,END+1):
    for month in range(1,13):
        for day in range(1,31):
            link = "https://www.federalreserve.gov/monetarypolicy/fomcminutes%i%02i%02i.htm" %(year,month,day)
            if check_link_exists(link):
                links.append(link)
            progressbar.update(1)
            progressbar.set_postfix(Message=f"Checking date {month}/{day}/{year}")

with open(TARGET, "w") as file:
    [file.write(link+"\n") for link in links]