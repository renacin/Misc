# Name:                                            Renacin Matadeen
# Date:                                               12/25/2021
# Title                         City Of Toronto: Graphics & Visualization File Crawler
#
# ----------------------------------------------------------------------------------------------------------------------
from Funcs.func import *
# ----------------------------------------------------------------------------------------------------------------------


def main():
    """ Main Logic Of File Crawler """

    # Create Instance Of File Crawler & Gather Data
    crawler = FileCrawler()
    crawler.gather_data(r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools")
    crawler.export_data()

    # Once All Files & Folders Have Been Crawled Return Data As CSV

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
