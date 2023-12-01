from getdates import *
from compiledata import *
import nltk

#call functions to get links, dates, and year-end dates
links, dates = get_links_and_dates()
year_end_dates = get_year_end_dates(dates)

#retrieve links for each year-end file
year_end_links = []
for year_end_date in year_end_dates:
    for link in links:
        if year_end_date in link:
            year_end_links.append(link.strip('\n'))

#list that stores all text for each year-end meeting, as a string, 1 element per year
year_end_meeting_text_list = text_webscrape(year_end_links)


#list of lists, each element is a list that stores all the links for each year
links_by_year = group_links_by_year(links)

cleaned_links_by_year = [[item.strip() for item in inner_list] for inner_list in links_by_year]

dataset_by_year = []
for links_per_year in cleaned_links_by_year:
    yearly_text = text_webscrape(links_per_year)
    dataset_by_year.append(yearly_text)
   

#for each string in 'dataset_by_year', we can strip everything up to "By unanimous vote" to get rid of the names, then join the sublists into one string to get all the text for one whole year  

#only for testing purposes
with open('text.txt', 'w') as file:
    # Iterate through the lists and write them to the file
    for sublist in dataset_by_year:
        line = ','.join(sublist)  # Assuming you want to separate items by commas
        file.write(line + 'NEXTLINE\n\n\n\n')

#DATASET1: 'year_end_meeting_text_list': List of text for each year-end meeting, each element contains a string of text for the year-end meeting.

#DATASET2: 'dataset_by_year': List of lists - each element is a list of text strings for all the meetings held for a year. ([[dec2008text], [jan2009text,mar2009text,may2009text], etc.])

#can now perform analysis on either dataset
#can analyze each year and see what kinds of words stay common, what words come and go in frequency ('recession', 'growth', etc.)
#can find collocations each year to see if those change 
#can look at year-end language vs year as a whole language, see if it differs at all
