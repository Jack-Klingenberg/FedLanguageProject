# Federal Reserve Language Project

Term project for CSCI2349. Analysis and language modeling for Federal Reserve Minutes.

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
  - [Guide](#guide)
  - [To-Do](#todo)

## Setup

To get the project up and running, clone the repository to your home directory and run "bash setup.sh" to create a virtual environment and install dependencies. You may want to do this manually if there are issues.

## Guide

#### Programs:

setup.sh - short shell script to create venv and install packages

requirements.txt - contains packages and versions needed for the project. If you install new packages, you need to add them to this document using "python3 -m pip freeze > requirements.txt". Note that the virtual environment must be active when you do this or else it will push all packages you have installed into requirementst.txt which is an issue.

savehtml.py - program that takes link file and output directory and saves all the html files locally

gatherlinks.py - python script that gets all documents in a specified date range and pushes them to a text file. Usage: python3 gatherlinks.py [start] [end] [filepath]

compiledata.py - deprecated python script that created a csv file indexed by the FOMC meeting (in time order)

gatherlinks.py - tests url endpoints to find all the required links to the meeting notes. The meeting notes are stored at identical URLs that only differ in the numbers at the end (which is just the date of the meeting), this script goes through and tests each endpoint in a given range storing all the "active" links in a text file.

tfidf.ipynb - python notebook where we created all of the graphs and tf-idf visualizations for the presentation

getdates.py - contains functions which are called when generating our datasets

generate_textbyyear.py - script to create the 'textbyyear.txt' file.

create_txtfilesbyyear.ipnyb - python notebook to create the txtfilesbyyear folder

analyze_by_year.py - read in dataset -> tokenize, create stop list, bigrams, collocations, word clouds

#### Data:

data (folder) - stores all the HTML files, as well as the csv file outputted by compiledata.py and some misc text files

alltxtfiles (folder) - all scraped FOMC meetings, each file is one meeting

txtfilesbyyear (folder) - all FOMC minutes combined into documents by year

textbyyear.txt - text per year, all in one .txt file

## To-Do

- [x] Generate links
- [x] Save links to html files
- [x] Write web scraper code for each webpage (!)
- [x] Compile all scraped text into dataset that can be loaded without repeating web scraping process
- [x] Analyze data
- [x] Create slides
- [x] Presentation
