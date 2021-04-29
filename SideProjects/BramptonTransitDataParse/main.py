# Name:                                            Renacin Matadeen
# Date:                                               04/25/2021
# Title                                   Brampton Transit But Location Parse
#
# ----------------------------------------------------------------------------------------------------------------------
from Funcs.functions import *
# ----------------------------------------------------------------------------------------------------------------------


def main():
    """ This function will define the main logic of this data collection experiment """

    # Instantiate webcrawler, and connect to databse
    Crawler = WebCrawler()
    SQLite_DB = SQLite_Database(r"DataStorage.db")

    # Constantly gather from JSON stream | Every 30 seconds?
    raw_data = Crawler.gather_transit_data()
    cleaned_data = Crawler.clean_transit_data(raw_data)
    weather_data = Crawler.gather_weather_data()

    # Append Data To Database
    SQLite_DB.addtoDB(weather_data, 2)


# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
