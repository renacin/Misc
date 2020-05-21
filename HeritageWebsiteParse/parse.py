# Name:                                            Renacin Matadeen
# Date:                                               05/20/2020
# Title                                          Heritage Website Parse
#
# ----------------------------------------------------------------------------------------------------------------------
import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# ----------------------------------------------------------------------------------------------------------------------


# Secondary Function | Grab IDs from text file
def grab_ids(text):

    # Find Every Entry That Has The Same Anchor Tags
    buildingid_pattern = r'BuildingID=\d+.>'
    listofids = list(re.findall(buildingid_pattern, text))

    return listofids


# Secondary Function | Create Webscraper Using Selenium
def parsedata(fullpath):
        # Setup Chrome Driver
        path = r"C:\Users\renac\Documents\Programming\Python\Selenium\chromedriver.exe"
        chrome = webdriver.Chrome(executable_path=path)

        # Visit Site
        chrome.get(fullpath)
        time.sleep(2)
        chrome.close()

# Main Function
def main():

    # Instantiate Path With Textfile containing entire html element with all entries
    path = r"C:\Users\renac\Documents\Programming\Python\Misc\HeritageWebsiteParse\listofschools.txt"
    text_file = open(path,'r')
    text_raw = text_file.read()

    # Grab IDs with RegEx
    listofids = grab_ids(text_raw)

    # With List Of IDs Iterate Through Each And Scrape Data, Append To An Awaiting DataDictionry
    website = "https://www.acotoronto.ca/show_building.php?"
    for ids in listofids:

        # Create Full Path
        cleaned_id = ids.replace('">', '')
        full_path = website + cleaned_id

        # Parse Data
        parsedata(full_path)

        break

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
