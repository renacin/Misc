# Name:                                            Renacin Matadeen
# Date:                                               11/29/2020
# Title                                 Toronto Police Auctions - Website Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import re
from selenium import webdriver
# ----------------------------------------------------------------------------------------------------------------------


# Create A WebCrawler Class
class WebCrawler():

    # Initial Function, Run When A WebCrawler Object Is Created
    def __init__(self):
        self.raw_html = ""
        path = r"C:\Users\renac\Documents\Programming\Python\Selenium\chromedriver.exe"
        self.chrome_driver = webdriver.Chrome(executable_path=path)



    # Navigate To Url
    def navigate_url(self, url):
        self.chrome_driver.get(url)
        self.raw_html = self.chrome_driver.page_source
        time.sleep(2)



    # Scrape Number Of Pages On Website
    def scrape_pages(self):
        if self.raw_html != "":
            print("Scraping Number Of Pages...")

            # Find The Pagination At The Bottom Of The Page Within The Raw HTML
            pagination_pattern = r'">([0-9]{1,2})</a>'
            page_html = re.findall(pagination_pattern, self.raw_html)

            return int(page_html[-1])

        else:
            print("No HTML Data To Scape Pages")



    # Scrape Listing IDs On A Given Webpage
    def scrape_ids(self):
        if self.raw_html != "":
            print("Scraping Data...")

        else:
            print("No HTML Data To Collect IDs")



    # Close WebCrawler
    def self_destruct(self):
        self.chrome_driver.quit()


# ----------------------------------------------------------------------------------------------------------------------

# A Function That Will Help The User Create An Associated Url Based On Thier Choice
def choose_url(choice):
    base_url = "https://www.policeauctionscanada.com/Browse/"
    cat_dict = {"Jewellery": "C160535", "Coins&Currency": "C6245132", "Electronics":"C161063"}

    # Return The First Page Of The Category
    return base_url + cat_dict[choice] + "?page=0"


# A Function That Will Instruct The WebCrawler To Scape The Number Of Pages On The Site
def get_num_pages(url):

    Web_Scraper = WebCrawler()
    Web_Scraper.navigate_url(url)
    num_pages = Web_Scraper.scrape_pages())
    Web_Scraper.self_destruct()

    return num_pages



# # Parse Listing ID
# def listing_ids(raw_html):
#
#     # Find All Instances Of Listings With Regular Expression Pattern
#     listing_pattern = r'/Listing/Details/(.*)" class="btn btn-primary'
#     instances = re.findall(listing_pattern, raw_html)
#
#     return instances
#
# # Parse Total Number Of Pages
# def num_pages(chrome_driver):
#     # How Many More Pages?
#     pages_html = chrome_driver.find_element_by_xpath('/html/body/main/div/div[2]/div[3]/ul')
#     pages_text = pages_html.text
#     for arrow in ["«", "»", " "]:
#         pages_text = pages_text.replace(arrow, "")
#
#     all_pages = pages_text.split("\n")
#     return all_pages[-2]
#
#
#
#
#
# # A Function That Will Use A ChromeDriver To Navigate To The Site Chosen
# def visit_site(url):
#
#
#     # Visit Site | Get Source HTML
#     chrome.get(url)
#     time.sleep(2)
#
#     # Grab Raw HTML
#     html_ = chrome.page_source
#
#     # Return Listing IDs As A List
#     listings = listing_ids(html_)
#
#     # Num Pages
#     print(num_pages(chrome))
#
#     # Close Web Driver
#     chrome.quit()

    # url = choose_url("Jewellery")
    # visit_site(url)

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":

    # Choose URL
    url = choose_url("Jewellery")

    # Navigate To Url & Get Number Of Pages
    num_pages = get_num_pages(url)
