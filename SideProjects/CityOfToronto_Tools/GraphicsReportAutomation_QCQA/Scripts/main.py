# Name:                                            Renacin Matadeen
# Date:                                               01/17/2022
# Title                        City Of Toronto: Graphics & Visualization File Crawler
#
# ----------------------------------------------------------------------------------------------------------------------
import os
import datetime
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


class QC_Checker:
    """ This class stores all functions of the Graphics & Visualization """

    # ------------------------------------------------------------------------------------------------------------------
    #   STATIC VARIABLES
    raw_data = None
    current_date = str(datetime.date.today().strftime("%Y-%m-%d")).split(" ")[0]


    # ------------------------------------------------------------------------------------------------------------------
    #   PRIVATE METHODS
    def __filechecker(self, file_path) -> bool:
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

        # Make Sure Path Points To File, Filename Is Appropriate, Is XLSX Doc, & Has Appropriate Headers/Footers
        if os.path.isdir(file_path) == False:
            if " ".join(file_path.split(".")[0].split()[3:]) == "All Applications Received - Extract":
                if (file_path.split(".")[-1] in ["xlsx", "XLSX"]):
                    print(file_path)

    # ------------------------------------------------------------------------------------------------------------------
    #   PUBLIC METHODS
    def gather_data(self, data_path: str) -> "None":
        """
        Notes:
            Given the path of the folder that contains all XLSX documents that contain addresses passed through
            the graphics request FME automation script, combine all XLSX documents into one Pandas Dataframe.
            Dataframe cached as class static variable.
            applications.

        Input:
            data_path: string --> Path To Folder Containing All XLSX documents

        Output:
            None: None --> Resulting dataframe is stored within Class as static variable. Use method to access.
        """

        # Given Path, Loop Through Folder & Combine XLSX Files | Ensure Checks For Appropriate Files!
        directory_ = os.listdir(data_path)
        for file_path in directory_:
            self.__filechecker(file_path)

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
