# Author: Jack Klingenberg 
# Date: Nov 24, 2023
# Description: Program that takes link file and output directory and saves all the html files locally

import sys
import requests
import os
import re

def save_html_to_file(url, filepath):
    with open(url, "r") as file:
        for link in file:
            try:
                response = requests.get(link.strip())
                response.raise_for_status() 

                fomc_date = link.split(r'fomcminutes')[-1].strip()[0:-4]
                
                with open(os.path.join(filepath, f'minutes{fomc_date}.html'), 'w', encoding='utf-8') as file:
                    file.write(response.text)

                print(f"HTML content successfully saved to {filepath}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <output_filepath>")
        sys.exit(1)

    link_file = sys.argv[1]
    output_path = sys.argv[2]

    save_html_to_file(link_file, output_path)
