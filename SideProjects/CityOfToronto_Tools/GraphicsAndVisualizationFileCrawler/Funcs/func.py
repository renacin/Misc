# Name:                                            Renacin Matadeen
# Date:                                               10/31/2021
# Title           Interval House Data Analytics Project: Canadian Census Data K-Means Clustering Attempt
#
# ----------------------------------------------------------------------------------------------------------------------
from datetime import date
import os
# ----------------------------------------------------------------------------------------------------------------------


class FileCrawler:
    """ This class stores all functions of this file crawler"""

    def __init__(self):
        """ On instantiation create a dictionary that will store parsed """

        self.crawler_storage = {
                                "Date": str(date.today().strftime("%d/%m/%Y")),
                                "PathsCrawled": [],
                                "Data": {}
                                }

    # ------------------------------------------------------------------------------------------------------------------
    #   PRIVATE METHODS
    def __recursive_crawl(self, path: str):
        """ Given a path, find files and parse data to storage. """

        # Iterate Through Files & Folders | Create Complete Path
        directory_ = os.listdir(path)
        for item in directory_:
            item_path = path + "\\" + item

            # If The Item Is A Folder Call Recursive Function
            if os.path.isdir(item_path):
                # Gather Some Data On Folders
                self.__write_data("Folder", item_path)
                self.__recursive_crawl(item_path)

            # The Item Is A File | Scrape All Data
            else:
                self.__write_data("File", item_path)


    def __write_data(self, obj_type: str, item_path: str):
        """ Given a file, gather as much usable information; write to storage. """

        if obj_type == "File":
            file_type = "." + item_path.split(".")[-1].upper()

        # print(str(os.stat(item_path)).split(","))


    # ------------------------------------------------------------------------------------------------------------------
    #   PUBLIC METHODS
    def gather_data(self, path: str):
        """ Given a path to a folder, this function will gather information on each file within that folder,
        using recursion to reach every file"""

        # Check To See If Path Links To Folder. If File Return Nothing | User Error
        cp_path = path
        if os.path.isdir(cp_path):
            self.__recursive_crawl(cp_path)

        else:
            return

        # Provided Paths +1
        if os.path.isdir(path):
            self.crawler_storage["PathsCrawled"].append(path)


    def export_data(self) -> "CSV":
        """ Once data has been collected this function will export data as a CSV for additional analysis """
        pass
