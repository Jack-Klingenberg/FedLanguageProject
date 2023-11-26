from getdates import *
from webscrape import *

#call functions to get links, dates, and year-end dates
links, dates = get_links_and_dates()
year_end_dates = get_year_end_dates(dates)

#retrieve links for each year-end file
year_end_links = []
for year_end_date in year_end_dates:
    for link in links:
        if year_end_date in link:
            year_end_links.append(link.strip('\n'))

#list to store all text for each year-end meeting, as a string, 1 element per year
year_end_meeting_text_list = text_webscrape(year_end_links)

#can now perform analysis on this list
#analyze each year and see what kinds of words stay common and what words come and go in frequency (maybe the word "recession" is more frequent in some years)
#can find collocations each year to see if those change