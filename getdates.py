# Author: Ben Elenbaas
# Description: Contains functions which are called when generating our datasets.

import re

# retrieves all of the urls, returns the links and dates of each meeting (comes directly from the links) 
def get_links_and_dates():
    links_txt_path = 'data/links.txt'
    with open(links_txt_path, 'r') as links_txt:
        links = links_txt.readlines()

    dates = []
    for link in links:
        file_date = re.sub('https://www.federalreserve.gov/monetarypolicy/fomcminutes', '', link)
        file_date = re.sub('.htm\n', '', file_date)
        dates.append(file_date)
    
    return links, dates

# get only the year-end dates; we didn't end up 
def get_year_end_dates(dates):
    year_end_dates = []
    for date in dates:
        # Check if the month is December (characters at positions 4 and 5)
        if date[4:6] == '12':
            year_end_dates.append(date)

    return year_end_dates

#function to group the given links by year
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