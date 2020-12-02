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


    # Navigate To Url | Get Newest HTML Data
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
            print("Scraping Data On Current Page...")

            # Find All Instances Of Listings With Regular Expression Pattern
            listing_pattern = r'/Listing/Details/(.*)" class="btn btn-primary'
            instances = re.findall(listing_pattern, self.raw_html)

            return instances

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
    num_pages = Web_Scraper.scrape_pages()
    Web_Scraper.self_destruct()

    # Return Number Of Pages
    return num_pages


# A Function That Will Instuct The Web Crawler Which Pages To Scape
def pages_to_scrape(num_pages, url):
    Web_Scraper = WebCrawler()

    # Place To Store IDs
    list_of_ids = []
    for num in range(num_pages):

        # Create New Url Based On Number Of Pages
        new_url = url[:-1] + str(num)
        Web_Scraper.navigate_url(new_url)
        list_of_ids.extend(Web_Scraper.scrape_ids())

    Web_Scraper.self_destruct()
    print(list_of_ids)

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":

    # Gather Data From Toronto Police Auction Website
    url = choose_url("Jewellery")
    num_pages = get_num_pages(url)
    pages_to_scrape(num_pages, url)
