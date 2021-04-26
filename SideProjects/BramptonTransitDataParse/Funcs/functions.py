# Name:                                            Renacin Matadeen
# Date:                                               04/25/2021
# Title                  Main functions used within data collection effort will be found in this file
#
# ----------------------------------------------------------------------------------------------------------------------
import os, sys, time
import json, requests

import pandas as pd
from bs4 import BeautifulSoup
# ----------------------------------------------------------------------------------------------------------------------


class WebCrawler:
    """ This class will store the answers to basic recursive python questions """

    def __init__(self):
        pass

    def gather_data(self, json_url):
        """ This function takes the JSON link associated with Brampton Transit's GTFS link and parses JSON data from the webpage"""

        res = requests.get(json_url)
        soup = str(BeautifulSoup(res.content, "lxml"))

        for str_rem in ["<html><body><p>", "</p></body></html>"]:
            soup = soup.replace(str_rem, "")
        all_data = json.loads(soup)

        entity_data = [data["vehicle"] for data in all_data["entity"]]
        return pd.DataFrame(entity_data)
