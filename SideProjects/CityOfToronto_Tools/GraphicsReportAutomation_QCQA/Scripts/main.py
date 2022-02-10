# Name:                                            Renacin Matadeen
# Date:                                               01/17/2022
# Title                        City Of Toronto: Graphics & Visualization File Crawler
#
# ----------------------------------------------------------------------------------------------------------------------
import os, datetime, csv

from itertools import cycle
from openpyxl.workbook import Workbook

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
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


    #   PRIVATE METHODS
    def __formatexcel(self, full_ex_path, temp_df) -> bool:
        """
        FILL IN LATER
        """

        # Write Data To Excel | Add Formatting!!!
        with pd.ExcelWriter(full_ex_path, engine='xlsxwriter') as writer:

            # Write Dataframe To Excel, Initial Formatting
            df_len = len(temp_df)
            temp_df.to_excel(writer, sheet_name="Formatted_Applications", index=False)

            # Grab Workbook & Sheet
            workbook  = writer.book
            worksheet = writer.sheets["Formatted_Applications"]

            # Add a header format & alternating format
            header_format = workbook.add_format({
                'italic': True,
                'bold': True,
                'bg_color': '#CCCCCC'
                })

            alt1 = workbook.add_format({
                'bg_color': '#EEEEEE'
                })

            alt2 = workbook.add_format({
                'bg_color': '#DDDDDD'
                })

            workspace_fmt = workbook.add_format({
                'border': True
                })

            # Write the column headers with the defined format
            header_range = "A1:H1"
            worksheet.conditional_format(header_range, {'type': 'cell',
                                                   'criteria': '>',
                                                   'value': -99999999999,
                                                   'format': header_format})

            # Format Alternating Rows
            formats = cycle([alt1, alt2])
            for row in range(2, df_len + 2):
                data_format = next(formats)

                # Focus Row Range
                x_row_range = f"A{row}:H{row}"
                worksheet.conditional_format(x_row_range, {'type': 'cell',
                                                       'criteria': '>',
                                                       'value': -99999999999,
                                                       'format': data_format})

            # Final WorkSheet Fomatting
            worksheet.freeze_panes(1, 0)
            total_range = f"A1:H{df_len + 1}"
            worksheet.conditional_format(total_range, {'type': 'cell',
                                                   'criteria': '>',
                                                   'value': -99999999999,
                                                   'format': workspace_fmt})

            del temp_df, writer




    # ------------------------------------------------------------------------------------------------------------------
    #   PUBLIC METHODS
    def gather_data(self, data_path: str) -> "None":
        """
        Notes:
            Given the path of the folder that contains all CSV documents that contain addresses passed through
            the graphics request FME automation script, combine all CSV documents into one Pandas Dataframe.
            Dataframe cached as class static variable.

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


    def check_data(self, export_path: str) -> "CSV":
        """
        Notes:
            If other older files are stored in the master output folder this function will compare the cached
            dataframe with the older data in that folder. If new columns, or cells are identified, they will be
            added to the cached dataframe.

        Input:
            export_path: string --> Path To Folder Where Data Will Be Exported

        Output:
            None --> Cached Dataframe is modified

        GENERAL CAUTION: IF PRESENT OLDER MASTER FILES WILL BE DELETED
        """

        # Look For Older Files In Export Folder
        directory_ = os.listdir(export_path)
        for file_ in directory_:
            split_name = file_.split("_")
            if file_.__contains__("COMMENTS"):
                print("_".join(split_name))


        # FIX THIS PLEASE!!!!!!!


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
                full_ex_path = export_path + "\\" + QC_Checker.current_date + "_QC_MasterFile_" + district.strip() + ".xlsx"

                # Drop Unneeded Columns
                col_to_keep = ["File Number", "Address", "InDate", "Folder Name"]
                for col in temp_df.columns:
                    if col not in col_to_keep:
                        temp_df.drop(col, axis=1, inplace=True)

                # Add Additional Columns
                col_to_add = ["QC_Status", "Comments", "Actions", "StaffName"]
                for new_col in col_to_add:
                    temp_df[new_col] = ""

                # Format Data
                self.__formatexcel(full_ex_path, temp_df)

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
    # qc_init.check_data(export_folder)
    qc_init.export_data(export_folder)
