# Name:                                            Renacin Matadeen
# Date:                                               04/25/2021
# Title                                   Brampton Transit But Location Parse
#
# ----------------------------------------------------------------------------------------------------------------------
from Funcs.functions import *
# ----------------------------------------------------------------------------------------------------------------------


def main():
    """ This function will define the main logic of this data collection experiment """

    # Create a WebCrawler Instance & Gather Data For Bus Locations
    Crawler = WebCrawler()
    raw_data = Crawler.gather_data("http://nextride.brampton.ca:81/API/VehiclePositions?format=json")

    # Clean Raw Data



# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
