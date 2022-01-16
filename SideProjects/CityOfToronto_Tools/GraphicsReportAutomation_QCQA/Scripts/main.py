# Name:                                            Renacin Matadeen
# Date:                                               01/17/2022
# Title                        City Of Toronto: Graphics & Visualization File Crawler
#
# ----------------------------------------------------------------------------------------------------------------------
import os
import datetime
import pandas as pd
import csv
# ----------------------------------------------------------------------------------------------------------------------


class QC_Checker:
    """ This class stores all functions of the Graphics & Visualization """

    # ------------------------------------------------------------------------------------------------------------------
    #   STATIC VARIABLES
    raw_data = None
    current_date = str(datetime.date.today().strftime("%Y-%m-%d")).split(" ")[0]


    # ------------------------------------------------------------------------------------------------------------------
    #   PRIVATE METHODS
    def __filechecker(self, file_, data_path) -> bool:
        """
        Notes:
            Checks are conducted to ensure the files provided fit the appropriate format:
                + XLSX
                + Contain Headers & Footers
                + Same Columns & Datatypes between files

        Input:
            file_path: string --> Path To File

        Output:
            bool: True/False --> Is the file appropriate, given requirements?
        """

        # Make Sure Path Points To File, Filename Is Appropriate, Is CSV Doc, & Has Appropriate Headers/Footers
        if os.path.isdir(file_) is False:
            if " ".join(file_.split(".")[0].split()[3:]) == "All Applications Received - Extract":
                if (file_.split(".")[-1] in ["csv", "CSV"]):
                    with open((data_path + "\\" + file_), mode ='r') as file:
                        csv_file = csv.reader(file)
                        for line in csv_file:
                            if line[0] == "IBMS Reports":
                                return True
        return False

    # ------------------------------------------------------------------------------------------------------------------
    #   PUBLIC METHODS
    def gather_data(self, data_path: str) -> "None":
        """
        Notes:
            Given the path of the folder that contains all CSV documents that contain addresses passed through
            the graphics request FME automation script, combine all CSV documents into one Pandas Dataframe.
            Dataframe cached as class static variable.
            applications.

        Input:
            data_path: string --> Path To Folder Containing All XLSX documents

        Output:
            None: None --> Resulting dataframe is stored within Class as static variable. Use method to access.
        """

        # Given Path, Loop Through Folder & Combine XLSX Files | Ensure Checks For Appropriate Files!
        directory_ = os.listdir(data_path)
        for file_ in directory_:
            print(file_)
            if self.__filechecker(file_, data_path):
                df = pd.read_csv((data_path + "\\" + file_), skiprows= 6)
                print(df)
                break

            else:
                print("Error")

        #
        # print(data_path)
        # print(QC_Checker.current_date)


# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point
if __name__ == "__main__":

    # Needed Variables
    df_path = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\GraphicsReportAutomation_QCQA\Data\WeeklyApplicationsLists"

    # Main Logic Of QC Checker
    qc_init = QC_Checker()
    qc_init.gather_data(df_path)
