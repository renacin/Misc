# Name:                                            Renacin Matadeen
# Date:                                               04/25/2021
# Title                  Main functions used within data collection effort will be found in this file
#
# ----------------------------------------------------------------------------------------------------------------------
import os, sys, time, re
import json, requests, ast

import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
# ----------------------------------------------------------------------------------------------------------------------


class WebCrawler:
    """ This class will gather data on both bus locations as well as weather data """


    def __init__(self):
        self.transit_url = "http://nextride.brampton.ca:81/API/VehiclePositions?format=json"
        self.weather_url = "https://forecast.weather.gov/data/obhistory/metric/CYYZ.html"


    def gather_weather_data(self):
        """ This function takes the weather link provided and grabs weather data for brampton """

        # Grab raw HTML data from weather page
        wea_html = requests.get(self.weather_url)
        df_list = pd.read_html(wea_html.text) # this parses all the tables in webpages to a list
        weather_df = df_list[3]
        weather_df = weather_df.iloc[3:4]

        # Change Column Names
        new_columns = ["Date", "Time", "Wind", "Visib", "Weather",
                       "SkyCond", "AirTemp", "DewPoint", "HrMax6",
                       "HrMin6", "RelHum", "WindChill", "HeatIndex",
                       "AltPres", "SeaPres", "Precip1hr", "Precitp3hr",
                       "Precip6hr"]

        weather_df.columns = new_columns
        return weather_df


    def gather_transit_data(self):
        """ This function takes the JSON link associated with Brampton Transit's GTFS link and parses JSON data from the webpage """

        # Grab data from JSON stream
        res = requests.get(self.transit_url)
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

        return df



# ----------------------------------------------------------------------------------------------------------------------


class SQLite_Database:
    """ This class will store both transit, and weather data """


    # Initial function, identify, or create a db in the location provided
    def __init__(self, db_location):
        try:
            # Connect to database check if it has data in it | Create two tables joined by primary key
            self.conn = sqlite3.connect(db_location)
            self.conn.execute('''CREATE TABLE IF NOT EXISTS TRANSIT_LOCATION_DB
                (congestion_level TEXT NOT NULL, current_status TEXT NOT NULL, current_stop_sequence TEXT NOT NULL,
                stop_id TEXT NOT NULL, timestamp TEXT NOT NULL, latitude TEXT NOT NULL, longitude TEXT NOT NULL,
                bearing TEXT NOT NULL, odometer TEXT NOT NULL, speed TEXT NOT NULL, trip_id TEXT NOT NULL,
                start_time TEXT NOT NULL, start_date TEXT NOT NULL, schedule_relationship TEXT NOT NULL,
                route_id TEXT NOT NULL, id TEXT NOT NULL, label TEXT NOT NULL, license_plate TEXT NOT NULL,
                weather_id TEXT NOT NULL);''')

            self.conn.execute('''CREATE TABLE IF NOT EXISTS WEATHER_DB
                (weather_id TEXT NOT NULL, Date TEXT NOT NULL, Time TEXT NOT NULL, Wind TEXT NOT NULL, Visib TEXT NOT NULL,
                Weather TEXT NOT NULL, SkyCond TEXT NOT NULL, AirTemp TEXT NOT NULL, DewPoint TEXT NOT NULL, HrMax6 TEXT NOT NULL,
                HrMin6 TEXT NOT NULL, RelHum TEXT NOT NULL, WindChill TEXT NOT NULL, HeatIndex TEXT NOT NULL, AltPres TEXT NOT NULL,
                SeaPres TEXT NOT NULL, Precip1hr TEXT NOT NULL, Precitp3hr TEXT NOT NULL, Precip6hr TEXT NOT NULL);''')

            print("Connected To Database")

        except sqlite3.OperationalError as e:
            print(e)


    # Function To Insert Data Into Database
    def addtoDB(self, parsed_data, table_num):
        cursor = self.conn.cursor()

        # Insert into bus location table
        if table_num == 1:
            cursor.execute("""INSERT INTO TPA_ITEM_DB(ITEM_NAME, SKU, CUR_PRICE, MIN_UPBID, UPBID_PRICE, MINUTES_LEFT, START_DATE, END_DATE, NUM_BIDS, HIGHEST_BIDR)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (parsed_data[0], parsed_data[1], parsed_data[2], parsed_data[3], parsed_data[4], parsed_data[5], parsed_data[6], parsed_data[7], parsed_data[8], parsed_data[9]))

        elif table_num == 2:
            cursor.execute("""INSERT INTO TPA_ITEM_DB(ITEM_NAME, SKU, CUR_PRICE, MIN_UPBID, UPBID_PRICE, MINUTES_LEFT, START_DATE, END_DATE, NUM_BIDS, HIGHEST_BIDR)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (parsed_data[0], parsed_data[1], parsed_data[2], parsed_data[3], parsed_data[4], parsed_data[5], parsed_data[6], parsed_data[7], parsed_data[8], parsed_data[9]))

        else:
            raise IndexError ("Table ID Out Of Index")

        self.conn.commit()
        cursor.close()
