# Name:                                            Renacin Matadeen
# Date:                                               04/25/2021
# Title                                   Brampton Transit But Location Parse
#
# ----------------------------------------------------------------------------------------------------------------------
from Funcs.functions import *
# ----------------------------------------------------------------------------------------------------------------------


def main():
    """ This function will define the main logic of this data collection experiment """

    # Create a WebCrawler Instance
    Crawler = WebCrawler("http://nextride.brampton.ca:81/API/VehiclePositions?format=json")

    # Constantly gather from JSON stream | Every 30 seconds?
    while True:
        try:
            raw_data = Crawler.gather_data()
            cleaned_data = Crawler.clean_data(raw_data)
            time.sleep(30)

        except Exception:
            break

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
