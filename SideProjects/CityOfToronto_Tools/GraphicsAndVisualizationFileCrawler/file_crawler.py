# Name:                                            Renacin Matadeen
# Date:                                               12/25/2021
# Title                        City Of Toronto: Graphics & Visualization File Crawler
#
# ----------------------------------------------------------------------------------------------------------------------
import datetime
import csv
import os
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


class FileCrawler:
    """ This class stores all functions of this file crawler"""

    # Private Variables


    def __init__(self):
        """ On instantiation create a dictionary that will store parsed """
        self.all_cols = ["Item_Path", "File Name", "Object Type", "File Type", "File Size (MB)", "Last Accessed", "Last Modified"]
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

        # Parse File Name
        filename = item_path.split("\\")[-1].split(".")[0]

        return last_acc, last_mod, file_size, filename


    def __write_data(self, obj_type: str, item_path: str):
        """ Given a file, gather as much usable information; write to crawler storage. """

        # Determine The File Type & Basic Details
        if obj_type == "File":
            file_type = "." + item_path.split(".")[-1].upper()
            last_acc, last_mod, file_size, filename= self.__str2data(item_path)

        else:
            file_type, last_acc, last_mod, file_size, filename = "", "", "", "", ""

        # Write Data To Internal Crawler Storage
        all_data = [item_path, filename, obj_type, file_type, file_size, last_acc, last_mod]
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

        # Make Sure The File Isn't Already Open
        try:
            # Check To See If File Already Exists | Delete If True
            if os.path.exists(out_path):
                os.remove(out_path)

            # Grab Data & Write Out To Provided Location
            data_df = pd.DataFrame.from_dict(self.crawler_storage["Data"])

            # Create Add Notes To CSV File
            with open(out_path, 'a', encoding='UTF8') as f:
                data_df.to_csv(out_path, index=False)
                writer = csv.writer(f)
                cur_date = self.crawler_storage["Date"]
                paths_crawled = self.crawler_storage["PathsCrawled"]

                writer.writerow("")
                writer.writerow(["Date Collected: ", cur_date])
                writer.writerow(["# Of Main Paths Searched: ", str(len(paths_crawled))])
                writer.writerow(["Main Paths Searched: ", paths_crawled])

        except PermissionError as err:
            print(err)


# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point
if __name__ == "__main__":

    # Create Instance Of File Crawler, Gather, & Export
    crawler = FileCrawler()
    crawler.gather_data(r"C:\Users\renac\Desktop\IH_Project")
    crawler.view_data()
    crawler.export_data(r"C:\Users\renac\Desktop\Data.csv")