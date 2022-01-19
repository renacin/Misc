# Name:                                            Renacin Matadeen
# Date:                                               01/17/2022
# Title                        City Of Toronto: Graphics & Visualization File Crawler
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

import os
import datetime
import csv
# ----------------------------------------------------------------------------------------------------------------------


class QC_Checker:
    """ This class stores all functions of the Graphics & Visualization """

    rd = None
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

        print(f"File Error Detected: {file_}")
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
            None --> Resulting dataframe is stored within Class as static variable. Use method to access.
        """

        # Given Path, Loop Through Folder & Combine CSV Files | Ensure Checks For Appropriate Files!
        frames = []
        directory_ = os.listdir(data_path)
        for file_ in directory_:
            if self.__filechecker(file_, data_path):
                add_df = pd.read_csv(data_path + "\\" + file_, skiprows= 6)
                for col in add_df.columns:
                    add_df[col] = add_df[col].astype(str)
                frames.append(add_df)

        merged_df = pd.concat(frames)
        merged_df = merged_df.drop_duplicates(subset = ["File Number"], keep = "first")
        QC_Checker.rd = merged_df


    def export_data(self, export_path: str) -> "CSV":
        """
        Notes:
            Given an export path, filter cached data by district name & create appropriate CSVs. If none are already
            there create new ones. If past versions are present combine & keep any new data provided by users.
            Caution, rows must be compared to master file already in file.

        Input:
            export_path: string --> Path To Folder Where Data Will Be Exported

        Output:
            CSVs --> A CSV For Each District
        """

        # Logic Check First | Export Data Based On District Type
        if str(type(QC_Checker.rd)) != "<class 'NoneType'>":
            for district in QC_Checker.rd["District"].unique():

                # Filter Data
                temp_df = QC_Checker.rd[QC_Checker.rd["District"] == district]
                full_ex_path = export_path + "\\" + QC_Checker.current_date + "_QC_MasterFile_" + district.strip() + ".csv"

                # Drop Unneeded Columns
                col_to_keep = ["File Number", "Address", "InDate", "Folder Name"]
                for col in temp_df.columns:
                    if col not in col_to_keep:
                        temp_df.drop(col, axis=1, inplace=True)

                # Add Additional Columns
                for new_col in ["QC_Status", "Comments", "Actions"]:
                    if new_col == "QC_Status":
                        temp_df[new_col] = "Not Checked"
                    else:
                        temp_df[new_col] = ""

                temp_df.to_csv(full_ex_path, index=False)
                del temp_df

                # TODO REMOVE DUPLICATES | HOW MANY REMOVED?????

            return

        print("Sequence Error Detected: First Load Data Into QC_Checker")


# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point
if __name__ == "__main__":

    # Needed Variables
    data_path = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\GraphicsReportAutomation_QCQA\Data\WeeklyApplicationsLists"
    export_folder = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\GraphicsReportAutomation_QCQA\Data\MasterOutputs"

    # Main Logic Of QC Checker
    qc_init = QC_Checker()
    qc_init.gather_data(data_path)
    qc_init.export_data(export_folder)
