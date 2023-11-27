#scrape the date off of each file

import re

def get_links_and_dates():
    #retrieve all of the urls
    links_txt_path = 'data/links.txt'
    with open(links_txt_path, 'r') as links_txt:
        links = links_txt.readlines()

    dates = []
    for link in links:
        file_date = re.sub('https://www.federalreserve.gov/monetarypolicy/fomcminutes', '', link)
        file_date = re.sub('.htm\n', '', file_date)
        dates.append(file_date)
    
    return links, dates

def get_year_end_dates(dates):
    year_end_dates = []
    for date in dates:
        # Check if the month is December (characters at positions 4 and 5)
        if date[4:6] == '12':
            year_end_dates.append(date)

    return year_end_dates

def group_links_by_year(links):
    grouped_links = []
    current_year = None
    current_group = []

    for link in links:
        match = re.search(r'https://www.federalreserve.gov/monetarypolicy/fomcminutes(\d{4})', link)
        if match:
            year = match.group(1)
            if year != current_year:
                if current_group:
                    grouped_links.append(current_group)
                current_group = [link]
                current_year = year
            else:
                current_group.append(link)

    if current_group:
        grouped_links.append(current_group)

    return grouped_links


#didn't initially realize that the numbers at the end of each url were the corresponding date 🤖
#we can save this for now in case we need to distinguish between the original/new url format for anything, else we can delete later
'''
the html changes from Dec. 2011 to Jan. 2012 - To measure change in language over time, we can go year by year, so we don't have to look at 100+ files. In order to separate year by year, we need a way to retrieve the year from each file, however the date location changes, so we can't just look at one place for all 100+ files.

#seperate urls by original/new format
original_html_links = []
new_html_links = []
for i, link in enumerate(links):
    if i < 32:
        original_html_links.append(link.strip())
    else:
        new_html_links.append(link.strip())

#get the dates for all the files with the original html format
original_dates = []
for url in original_html_links:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    for info in soup.find_all("title"):
        file_date = re.sub('FRB: FOMC Minutes, ', '', info.get_text())
        original_dates.append(file_date)

#get the dates for all the files with the new html format
new_dates = []
for url in new_html_links:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    for info in soup.find_all("")
'''