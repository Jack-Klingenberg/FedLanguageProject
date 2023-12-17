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

setup.sh - short shell script to create venv and install packages

requirements.txt - contains packages and versions needed for the project. If you install new packages, you need to add them to this document using "python3 -m pip freeze > requirements.txt". Note that the virtual environment must be active when you do this or else it will push all packages you have installed into requirementst.txt which is an issue.

gatherlinks.py - python script that gets all documents in a specified date range and pushes them to a text file. Usage: python3 gatherlinks.py [start] [end] [filepath]

compiledata.py - deprecated python script that created a csv file indexed by the FOMC meeting (in time order) 

gatherlinks.py - tests url endpoints to find all the required links to the meeting notes. The meeting notes are stored at identical URLs that only differ in the numbers at the end (which is just the date of the meeting), this script goes through and tests each endpoint in a given range storing all the "active" links in a text file. 

tfidf.ipynb - python notebook where we created all of the graphs for the presentation

data (folder) - stores all the HTML files, as well as the csv file outputted by compiledata.py and some misc text files

txtfilesbyyear (folder) - all FOMC minutes combined into documents by year 

## To-Do

- [x] Generate links
- [x] Save links to html files
- [x] Write web scraper code for each webpage (!)
- [x] Compile all scraped text into dataset that can be loaded without repeating web scraping process
- [x] Analyze data
- [x] Create slides
- [x] Presentation
