# Name:                                            Renacin Matadeen
# Date:                                               03/24/2022
# Title                     City Of Toronto: Graphics & Visualization Report Automation QA/QC Tool
#
# ----------------------------------------------------------------------------------------------------------------------
import os, datetime, csv
from itertools import cycle
from openpyxl.workbook import Workbook
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# ----------------------------------------------------------------------------------------------------------------------
#   PRIVATE FUNCTION
def __standardize_date(in_dates: list) -> list:
    """
    Notes:
        Identified an issue with date format going from Excel to CSV, and back to Excel.
        This private function will standardize the dates to a single format.

        Date Formats Found:
            1) [YYYY-MM-DD]
            2) [DD/MM/YYYY]
            3) [MM-DD-YYYY]

        Standardized Date Format:
            1) [YYYY-MM-DD]

    Input:
        in_dates:        Pandas Column -->    List of dates that needs to be standardized

    Output:
        out_dates:       list          -->    Cleaned list of dates
    """

    cleaned_dates = []
    for date_ in in_dates.values.tolist():

        # [DD/MM/YYYY]
        if "/" in date_:
            sep_date = date_.split("/")
            year_ = sep_date[-1]
            month_ = sep_date[1]
            day_ = sep_date[0]

        else:
            sep_date = date_.split("-")

            # [MM-DD-YYYY]
            if date_[-4:].isnumeric():
                year_ = sep_date[-1]
                month_ = sep_date[0]
                day_ = sep_date[1]

            # [YYYY-MM-DD]
            else:
                year_ = sep_date[0]
                month_ = sep_date[1]
                day_ = sep_date[-1]

        # [YYYY-MM-DD]
        cleaned_dates.append(f"{year_}-{month_}-{day_}")

    return cleaned_dates



# ------------------------------------------------------------------------------------------------------------------
#   PUBLIC FUNCTION
def gather_data(data_path: str, export_folder: str) -> "None":
    """
    Notes:
        Given the path of the folder that contains all CSV documents that contain addresses passed through
        the graphics request FME automation script, combine all CSV documents into one Pandas Dataframe.
        Dataframe cached as class static variable.

    Input:
        data_path:       string -->    Path To Folder Containing Weekly Update Xlsx Files
        export_folder:   string -->    Path To Folde Containing 4 District Output Files

    Output:
        Pandas DF --> Resulting dataframe, must up to date version

    Update:
        [2022-03-24 | Renacin Matadeen ] - Added Functionality To Create 1 masterfile from both weekly
                                           application list, as well as all 4 district outputs

    """

    # Given Path, Loop Through Folder & Combine CSV Files | Ensure Checks For Appropriate Files!
    frames = []
    directory_ = os.listdir(data_path)
    for file_ in directory_:
        if "~$" not in str(file_):
            weekly_df = pd.read_csv(data_path + "\\" + file_, skiprows= 6)
            for col in weekly_df.columns:
                weekly_df[col] = weekly_df[col].astype(str)
            frames.append(weekly_df)

    w_merged_df = pd.concat(frames)
    weekly_merged_df = w_merged_df.drop_duplicates(subset = ["File Number"], keep = "first")
    weekly_merged_df["InDate"] = __standardize_date(weekly_merged_df["InDate"])

    # Drop Unneeded Columns
    col_to_keep = ["File Number", "Address", "InDate", "Folder Name"]
    for col in weekly_merged_df.columns:
        if col not in col_to_keep:
            weekly_merged_df.drop(col, axis=1, inplace=True)


    # Look For All 4 District Files & Concatinate Back Into 1 File
    m_frames = []
    directory_ = os.listdir(export_folder)
    for d_file in directory_:

        # Skip If File Is Excel temp File
        if "~$" not in str(d_file):
            district_df = pd.read_excel(export_folder + "\\" + d_file)

            # Format Columns To String & Create New Dataset
            for col in district_df.columns:
                district_df[col] = district_df[col].astype(str)
            m_frames.append(district_df)

    districts_merged_df = pd.concat(m_frames)
    districts_merged_df = districts_merged_df.replace("nan", "")
    districts_merged_df = districts_merged_df.drop_duplicates(subset = ["File Number"], keep = "first")
    districts_merged_df["InDate"] = __standardize_date(districts_merged_df["InDate"])

    # Merge Both Files, Keep Note Of What Is Common, And What Is New
    combined_df = weekly_merged_df.merge(districts_merged_df, on=["File Number", "Address", "InDate"], how='outer', indicator=True)
    new_data_df = combined_df[combined_df["_merge"] == "left_only"]
    new_data_df.drop("_merge", axis=1, inplace=True)
    new_data_df.drop("Folder Name_y", axis=1, inplace=True)
    new_data_df.rename(columns = {"Folder Name_x": "Folder Name"}, inplace = True)

    # Final Database With New Content, Rows, & User Inputs
    final_df = pd.concat([new_data_df, districts_merged_df])

    return final_df




# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point
if __name__ == "__main__":

    # Needed Variables
    data_path = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\GraphicsReportAutomation_QCQA\Data\WeeklyApplicationsLists"
    export_folder = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\GraphicsReportAutomation_QCQA\Data\MasterOutputs"
    masterfile_export = r"C:\Users\renac\Desktop"

    # Gather Data & Write Master File
    all_data = gather_data(data_path, export_folder)
    all_data.to_csv(r"C:\Users\renac\Desktop\TEST.csv", index = False)





    # # qc_init.check_data(export_folder)
    # qc_init.export_data(export_folder)

    # current_date = str(datetime.date.today().strftime("%Y-%m-%d")).split(" ")[0]
