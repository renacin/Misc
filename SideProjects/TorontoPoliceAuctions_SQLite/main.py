# Name:                                            Renacin Matadeen
# Date:                                               11/29/2020
# Title                                 Toronto Police Auctions - Website Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import re
from selenium import webdriver
# ----------------------------------------------------------------------------------------------------------------------


# A Function That Will Help The User Create An Associated Url Based On Thier Choice
def choose_url(choice):
    base_url = "https://www.policeauctionscanada.com/Browse/"
    cat_dict = {"Jewellery": "C160535", "Coins&Currency": "C6245132", "Electronics":"C161063"}

    # Return The First Page Of The Category
    return base_url + cat_dict[choice] + "?page=0"



# Parse Listing ID
def listing_ids(raw_html):

    # Find All Instances Of Listings With Regular Expression Pattern
    listing_pattern = r'/Listing/Details/(.*)" class="btn btn-primary'
    instances = re.findall(listing_pattern, raw_html)

    return instances

# Parse Total Number Of Pages
def num_pages(chrome_driver):
    # How Many More Pages?
    pages_html = chrome_driver.find_element_by_xpath('/html/body/main/div/div[2]/div[3]/ul')
    pages_text = pages_html.text
    for arrow in ["«", "»", " "]:
        pages_text = pages_text.replace(arrow, "")

    all_pages = pages_text.split("\n")
    return all_pages[-2]





# A Function That Will Use A ChromeDriver To Navigate To The Site Chosen
def visit_site(url):
    # Setup Chrome Driver
    path = r"C:\Users\renac\Documents\Programming\Python\Selenium\chromedriver.exe"
    chrome = webdriver.Chrome(executable_path=path)

    # Visit Site | Get Source HTML
    chrome.get(url)
    time.sleep(2)

    # Grab Raw HTML
    html_ = chrome.page_source

    # Return Listing IDs As A List
    listings = listing_ids(html_)

    # Num Pages
    print(num_pages(chrome))

    # Close Web Driver
    chrome.quit()

# ----------------------------------------------------------------------------------------------------------------------


# Main Function That Will Do Everything
def main():
    url = choose_url("Jewellery")
    visit_site(url)

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
