# Name:                                            Renacin Matadeen
# Date:                                               11/29/2020
# Title                                 Toronto Police Auctions - Website Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
from wc import WebCrawler
# ----------------------------------------------------------------------------------------------------------------------

# A Function That Will Help The User Create An Associated Url Based On Thier Choice
def choose_url(choice):
    base_url = "https://www.policeauctionscanada.com/Browse/"
    cat_dict = {"Jewellery":"C160535", "Coins&Currency":"C6245132", "Electronics":"C161063", "Art&Antiques":"C632998"}

    # Return The First Page Of The Category
    return base_url + cat_dict[choice] + "?page=0"


# A Function That Will Instruct The WebCrawler To Scape The Number Of Pages On The Site
def get_num_pages(url):

    Web_Scraper = WebCrawler()
    Web_Scraper.navigate_url(url)
    num_pages = Web_Scraper.scrape_pages()
    Web_Scraper.self_destruct()

    # Return Number Of Pages
    print("Total Number Of Pages Gathered")
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

        print("IDs Scraped From Page: {}".format(num+1))

    Web_Scraper.self_destruct()
    return list_of_ids


# A Function That Will Visit Each Item ID & Gather Data
def visit_unique_item(list_of_item_ids):
    Web_Scraper = WebCrawler()

    # Visit Each Item, Gather Unique Data & Append To An Already Waiting SQL Lite Database
    for item_id in list_of_item_ids:
        full_url = "https://www.policeauctionscanada.com/Listing/Details/" + str(item_id)
        Web_Scraper.navigate_url(full_url)
        item_data = Web_Scraper.scrape_data()

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":

    # Ask WebCrawler To Check If An Operable Database Is Connected? If Not Ask It To Create One
    # TODO CONNECT TO SQL-LITE Database 

    # # Gather Data From Toronto Police Auction Website
    # url = choose_url("Jewellery")
    # num_pages = get_num_pages(url)
    # list_of_ids = pages_to_scrape(num_pages, url)
    # visit_unique_item(list_of_ids)
