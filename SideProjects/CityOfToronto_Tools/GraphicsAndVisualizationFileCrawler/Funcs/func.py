# Name:                                            Renacin Matadeen
# Date:                                               12/25/2021
# Title                        City Of Toronto: Graphics & Visualization File Crawler
#
# ----------------------------------------------------------------------------------------------------------------------
import datetime
import os
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


class FileCrawler:
    """ This class stores all functions of this file crawler"""

    # Private Variables


    def __init__(self):
        """ On instantiation create a dictionary that will store parsed """
        self.all_cols = ["Item_Path", "Object Type", "File Type", "File Size (MB)", "Last Accessed", "Last Modified"]
        self.crawler_storage = {
                                "Date": str(datetime.date.today().strftime("%d/%m/%Y")),
                                "PathsCrawled": [],
                                "Data": {}
                                }

        for col in self.all_cols:
            self.crawler_storage["Data"][col] = []

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


    def __str2data(self, item_path: str) -> "Dictionary Row":
        """ Given a string, parse out & format important details about file """

        # Parse File Size, Date Created Info (In KB, & Date Formats)
        rd_1 = str(os.stat(item_path))
        for correction in ["os.stat_result(", ")", " "]:
            rd_1 = rd_1.replace(correction, "")

        # Find Important Information (File Size (In MB), Date Created, Modified, Etc...)
        stat_names = [(x.split("="))[0] for x in rd_1.split(",")]
        stat_vals = [(x.split("="))[-1] for x in rd_1.split(",")]
        stat_dict = dict(zip(stat_names, stat_vals))

        last_acc = str(datetime.datetime.fromtimestamp(int(stat_dict["st_atime"])))
        last_mod = str(datetime.datetime.fromtimestamp(int(stat_dict["st_mtime"])))
        file_size = round((int(stat_dict["st_size"]) / 1000000), 4)

        return last_acc, last_mod, file_size


    def __write_data(self, obj_type: str, item_path: str):
        """ Given a file, gather as much usable information; write to crawler storage. """

        # Determine The File Type & Basic Details
        if obj_type == "File":
            file_type = "." + item_path.split(".")[-1].upper()
            last_acc, last_mod, file_size = self.__str2data(item_path)

        else:
            file_type, last_acc, last_mod, file_size = "", "", "", ""

        # Write Data To Internal Crawler Storage
        all_data = [item_path, obj_type, file_type, file_size, last_acc, last_mod]
        for name, data_entry in zip(self.all_cols, all_data):
            self.crawler_storage["Data"][name].append(data_entry)


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


    def view_data(self):
        """ Print data as Pandas Dataframe """

        data_df = pd.DataFrame.from_dict(self.crawler_storage["Data"])
        print(data_df)


    def export_data(self, out_path: str) -> "CSV":
        """ Once data has been collected this function will export data as a CSV for additional analysis """

        # Grab Data & Write Out To Provided Location
        data_df = pd.DataFrame.from_dict(self.crawler_storage["Data"])
        data_df.to_csv(out_path, index=False)
