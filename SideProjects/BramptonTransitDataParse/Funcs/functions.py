# Name:                                            Renacin Matadeen
# Date:                                               04/25/2021
# Title                  Main functions used within data collection effort will be found in this file
#
# ----------------------------------------------------------------------------------------------------------------------
import os, sys, time
import json, requests

import ast
import pandas as pd
from bs4 import BeautifulSoup
# ----------------------------------------------------------------------------------------------------------------------


class WebCrawler:
    """ This class will store the answers to basic recursive python questions """


    def __init__(self, json_url):
        self.jurl = json_url


    def gather_data(self):
        """ This function takes the JSON link associated with Brampton Transit's GTFS link and parses JSON data from the webpage """

        # Grab data from JSON stream
        res = requests.get(self.jurl)
        soup = str(BeautifulSoup(res.content, "lxml"))

        # Clean up html tags
        for str_rem in ["<html><body><p>", "</p></body></html>"]:
            soup = soup.replace(str_rem, "")
        all_data = json.loads(soup)

        # Prepare for Pandas DF & Return
        entity_data = [data["vehicle"] for data in all_data["entity"]]
        return [data["vehicle"] for data in all_data["entity"]]


    def clean_data(self, raw_data):
        """ This function takes the parsed JSON data, cleans it and returns as a pandas dataframe """

        # Create pandas DF with data
        df = pd.DataFrame(raw_data)

        # Expand columns that contain data as dicts
        for col_2_xpand in ["position", "trip", "vehicle"]:

            # Expand column data into dictionary
            temp_df = df[col_2_xpand].astype("str")
            temp_df = temp_df.apply(lambda x: ast.literal_eval(x))
            temp_df = temp_df.apply(pd.Series)

            # Add columns to orginal dataset & remove old columns
            df = pd.concat([df, temp_df], axis=1)
            df.drop(columns=[col_2_xpand], inplace=True)

        print(len(df))

        return df