import sys
import csv

def read_in_data():
    lines = []
    with open('data/ds1.csv', 'r') as csv_file, open('text.txt', 'w') as out_file:
        for line in csv_file:
            out_file.write(line.strip())
            lines.append(line.strip())
    return lines

#'lines' is a list of string of all the text per html file
#can now tokenize