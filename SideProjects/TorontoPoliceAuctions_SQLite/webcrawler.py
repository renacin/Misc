# Name:                                            Renacin Matadeen
# Date:                                               11/29/2020
# Title                                 Toronto Police Auctions - Website Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# ----------------------------------------------------------------------------------------------------------------------


# Create A WebCrawler Class
class WebCrawler():

    # Initial Function, Run When A WebCrawler Object Is Created
    def __init__(self):
        self.raw_html = ""
        path = r"C:\Users\renac\Documents\Programming\Python\Selenium\chromedriver.exe"

        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # 'javascript': 2,
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2,
                                    'plugins': 2, 'popups': 2, 'geolocation': 2,
                                    'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                                    'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                    'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                                    'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                    'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                                    'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                                    'durable_storage': 2}}
        chrome_options.add_experimental_option('prefs', prefs)

        self.chrome_driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)


    # Navigate To Url | Get Newest HTML Data
    def navigate_url(self, url):
        self.chrome_driver.get(url)
        self.raw_html = self.chrome_driver.page_source
        time.sleep(2)


    # Scrape Number Of Pages On Website
    def scrape_pages(self):
        if self.raw_html != "":

            # Find The Pagination At The Bottom Of The Page Within The Raw HTML
            pagination_pattern = r'">([0-9]{1,2})</a>'
            page_html = re.findall(pagination_pattern, self.raw_html)
            return int(page_html[-1])

        else:
            print("No HTML Data To Scape Pages")


    # Scrape Listing IDs On A Given Webpage
    def scrape_ids(self):
        if self.raw_html != "":

            # Find All Instances Of Listings With Regular Expression Pattern
            listing_pattern = r'/Listing/Details/(.*)" class="btn btn-primary'
            instances = re.findall(listing_pattern, self.raw_html)
            return instances

        else:
            print("No HTML Data To Collect IDs")






    # Scrape Data On Individual Item
    def scrape_data(self):
        if self.raw_html != "":


            # Find Name Info | Use Regular Expression, Quicker?
            try:
                re_name = r'title">(.*)<img src'
                re_name_data = re.findall(re_name, self.raw_html)
                item_name = re_name_data[0]

                re_TPA_ID = r'\(([0-9]{1,7}.)\)'
                re_TPA_ID_data = re.findall(re_TPA_ID, item_name)
                item_TPA_ID = re_TPA_ID_data[0]

                full_TPA_ID = "(" + str(item_TPA_ID) + ")"
                item_name = item_name.replace(full_TPA_ID, "")
                item_name = item_name.replace("&amp;", "&")

                re_cur_price = r'Part">(.{1,10})</span>'
                re_cur_price_data = re.findall(re_cur_price, self.raw_html)
                parsed_prices = re_cur_price_data

                cur_price = re_cur_price_data[0]
                min_upbid = re_cur_price_data[1]
                upbid_increase = float(min_upbid) - float(cur_price)


            except:
                item_name = "N/A"
                item_TPA_ID = "N/A"
                item_price = "N/A"

                cur_price = "N/A"
                min_upbid = "N/A"
                upbid_increase = "N/A"


            # Find Bidding Info | Use Selenium Select By Xpath
            time_remaining_raw = self.chrome_driver.find_element_by_xpath('/html/body/main/div/div[2]/div/div[3]/div[3]/div[1]/span/span')
            rem_time_raw = time_remaining_raw.get_attribute('innerHTML')

            for rep_chr in ["Days", "Day"]:
                rem_time_raw = rem_time_raw.replace(rep_chr, "")
            rem_time_data = rem_time_raw.split("  ")

            print(rem_time_data)


        else:
            print("No HTML Data To Data Mine")







    # Close WebCrawler
    def self_destruct(self):
        self.chrome_driver.quit()
