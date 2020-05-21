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

        # Grab Location Data | Match With Search Pattern
        location_path = chrome.find_element_by_xpath("//*[@id=\"container\"]/div[7]/div[2]/span")
        location_text = location_path.get_attribute('innerText')

        try:
            loc_info = location_text.split("\n")
            name_ = loc_info[0]
            addr_ = loc_info[1]
            genloc_ = loc_info[2]

        except:
            name_ = fullpath
            addr_ = ""
            genloc_ = ""

        # Grab Construction Data | Match With Search Pattern
        construction_path = chrome.find_element_by_xpath("//*[@id=\"container\"]/div[11]")
        construction_text = construction_path.get_attribute('innerText')

        try:
            year_info = construction_text.split("\n")
            year_ = year_info[1]

        except:
            year_ = ""


        # Close Driver & Append Data
        chrome.close()
        print("School: {}, Address: {}, Neighbourhood: {}, Construction Date: {}".format(name_, addr_, genloc_, year_))
        return name_, addr_, genloc_, year_


# Main Function
def main():

    # Instantiate Path With Textfile containing entire html element with all entries
    path = r"C:\Users\renac\Documents\Programming\Python\Misc\HeritageWebsiteParse\listofschools.txt"
    text_file = open(path,'r')
    text_raw = text_file.read()

    # Grab IDs with RegEx
    listofids = grab_ids(text_raw)

    # Dictionary That Will Store Everything
    data_dictionary = {"School": [], "Address": [], "Neighbourhood": [], "Construction": []}

    # With List Of IDs Iterate Through Each And Scrape Data, Append To An Awaiting DataDictionry
    website = "https://www.acotoronto.ca/show_building.php?"
    for ids in listofids:

        # Create Full Path
        cleaned_id = ids.replace('">', '')
        full_path = website + cleaned_id

        # Parse Data
        name_, addr_, genloc_, year_ = parsedata(full_path)

        # Append To Dictionary
        data_dictionary["School"].append(name_)
        data_dictionary["Address"].append(addr_)
        data_dictionary["Neighbourhood"].append(genloc_)
        data_dictionary["Construction"].append(year_)
        break

    # Write Data To CSV
    final_df = pd.DataFrame.from_dict(data_dictionary)
    final_df.to_csv(r"C:\Users\renac\Desktop\CityPatternsProject\SchoolConstructionDates.csv", index=False)
    print("Finished Writting")

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
