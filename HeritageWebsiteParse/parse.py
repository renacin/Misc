# Name:                                            Renacin Matadeen
# Date:                                               05/20/2020
# Title                                          Heritage Website Parse
#
# ----------------------------------------------------------------------------------------------------------------------
import re
import time
import pandas as pd
from selenium import webdriver
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

        # Visit Site | Get Source HTML
        chrome.get(fullpath)
        time.sleep(2)
        html_ = chrome.page_source

        # Using RegEx Find Location
        location_pattern = r'<span style="line-height:1em;"><b>(.*)</span>'
        instances = re.findall(location_pattern, html_)

        # Clean Location Data
        instance = instances[0]
        instance = instance.replace("</b><br> ", "\n")
        instance = instance.replace("<br>", "\n")
        instances = instance.split("\n")

        name_ = instances[0]
        addr_ = instances[1]
        neigh_ = instances[2]

        # Using RegEx Find Date Of Construction
        construct_pattern = r'#333333;">(\s?.{5,50}\s?)</div>'
        construction_texts = re.findall(construct_pattern, html_)
        year_pattern = r'[0-9]{4}'

        # Have A helper Counter
        counter = 0
        for text in construction_texts:
            y_pattern = re.findall(year_pattern, text)

            try:
                yb = y_pattern[0]
                counter += 1

            except:
                pass

        if (counter > 0):
            yearbuilt_ = yb

        else:
            yearbuilt_ = ""

        # Close Driver & Append Data
        chrome.close()
        print("School: {}, Address: {}, Neighbourhood: {}, Construction Date: {}".format(name_, addr_, neigh_, yearbuilt_))
        return name_, addr_, neigh_, yearbuilt_


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
        name_, addr_, neigh_, yearbuilt_ = parsedata(full_path)


        # Append To Dictionary
        data_dictionary["School"].append(name_)
        data_dictionary["Address"].append(addr_)
        data_dictionary["Neighbourhood"].append(neigh_)
        data_dictionary["Construction"].append(yearbuilt_)

    # Write Data To CSV
    final_df = pd.DataFrame.from_dict(data_dictionary)
    final_df.to_csv(r"C:\Users\renac\Desktop\CityPatternsProject\SchoolConstructionDates.csv", index=False)
    print("Finished Writting")

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
