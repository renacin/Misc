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
            2) [MM/DD/YYYY]
            3) [MM-DD-YYYY]

        Standardized Date Format:
            1) [YYYY-MM-DD]

    Input:
        in_dates:        Pandas Column -->    List of dates that needs to be standardized

    Output:
        out_dates:              list   -->    Cleaned list of dates
    """

    cleaned_dates = []
    for date_ in in_dates.values.tolist():

        # [MM/DD/YYYY]
        if "/" in date_:
            sep_date = date_.split("/")
            year_ = sep_date[-1]
            month_ = sep_date[0]
            day_ = sep_date[1]

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


#   PRIVATE METHODS
def __formatexcel(full_ex_path, temp_df):
    """
    Notes:
        Given an export path, as well as a pandas dataframe containing cleaned & up-to-date excel data
        this function will add additional formatting

    Input:
        full_ex_path:        Export Path String  -->    Where will the district excel file be written to
        temp_df:             Pandas Dataframe    -->    The data that will be used to create the excel file

    Output:
        Output Excel:          ExcelFile XLSX    -->    The final excel file ready for district updates
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
        header_format = workbook.add_format({'italic': True, 'bold': True, 'bg_color': '#CCCCCC' })
        alt1 = workbook.add_format({'bg_color': '#EEEEEE'})
        alt2 = workbook.add_format({'bg_color': '#DDDDDD'})
        workspace_fmt = workbook.add_format({'border': True})

        # Write the column headers with the defined format
        header_range = "A1:I1"
        worksheet.conditional_format(header_range, {'type': 'cell', 'criteria': '>', 'value': -99999999999, 'format': header_format})

        # Format Alternating Rows
        formats = cycle([alt1, alt2])
        for row in range(2, df_len + 2):
            data_format = next(formats)

            # Focus Row Range
            x_row_range = f"A{row}:I{row}"
            worksheet.conditional_format(x_row_range, {'type': 'cell', 'criteria': '>', 'value': -99999999999, 'format': data_format})

        # Final WorkSheet Fomatting
        worksheet.freeze_panes(1, 0)
        total_range = f"A1:I{df_len + 1}"
        worksheet.conditional_format(total_range, {'type': 'cell', 'criteria': '>', 'value': -99999999999, 'format': workspace_fmt})

        # Add Data Validation | Column E QC Status
        row_range = f"E2:E{df_len + 1}"
        worksheet.data_validation(row_range, {'validate': 'list', 'source': ["Not Checked", "In Progress", "Checked"]})

        # Add Data Validation | Column G Actions Taken
        row_range = f"G2:G{df_len + 1}"
        worksheet.data_validation(row_range, {'validate': 'list', 'source': ["Completed edits - ready to go", "Working on edits", "Edits not started"]})


        # Add Data Validation | Column H Design Tech Name
        row_range = f"I2:I{df_len + 1}"
        worksheet.data_validation(row_range, {'validate': 'list', 'source': ["Not Checked", "In Progress", "Checked"]})

        del temp_df, writer



# ------------------------------------------------------------------------------------------------------------------
#   PUBLIC FUNCTION
def gather_data(data_path: str, export_folder: str) -> "None":
    """
    Notes:
        Given the path of the folder that contains all CSV documents that contain addresses passed through
        the graphics request FME automation script, combine all CSV documents into one Pandas Dataframe.
        Dataframe cached as class static variable.

    Input:
        data_path:                   string -->    Path To Folder Containing Weekly Update Xlsx Files
        export_folder:               string -->    Path To Folde Containing 4 District Output Files

    Output:
        Pandas DF:         Pandas Dataframe -->    Resulting dataframe, must up to date version

    Update:
        [2022-03-24 | Renacin Matadeen ] - Added Functionality To Create 1 masterfile from both weekly
                                           application list, as well as all 4 district outputs

    """

    # Given Path, Loop Through Folder & Combine CSV Files | Ensure Checks For Appropriate Files!
    frames = []
    directory_ = os.listdir(data_path)
    for file_ in directory_:
        if "~$" not in str(file_):
            weekly_df = pd.read_excel(data_path + "\\" + file_, skiprows= 6)
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

    # Final Database With New Content, Rows, & User Inputs | Sort Dataframe By InDate
    final_df = pd.concat([new_data_df, districts_merged_df])
    final_df["InDate"] = pd.to_datetime(final_df["InDate"])
    final_df.sort_values(by="InDate", inplace=True)

    # Create A Column That Identifies District
    district_list = []
    fold_num_list = final_df["File Number"].values.tolist()
    for f_num in fold_num_list:
        f_num_s = f_num.split(" ")
        district_list.append(f_num_s[2])

    final_df["District"] = district_list
    return final_df



def export_data(master_df, export_path, current_date):
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

    for district in master_df["District"].unique():
        if str(district) != "nan":

            # Filter By District
            temp_df = master_df[master_df["District"] == district]
            full_ex_path = export_path + "\\" + current_date + "_QC_MasterFile_" + district.strip() + ".xlsx"

            # Drop Unneeded Columns
            temp_df.drop("District", axis=1, inplace=True)

            # Add Additional Columns If Not Already Present
            new_cols = ["QC_Status", "Comments", "Actions", "StaffName", "CheckedByValen"]
            for n_col in new_cols:
                if n_col not in temp_df.columns:
                    temp_df[n_col] = ""

            # Format Data
            __formatexcel(full_ex_path, temp_df)



# ----------------------------------------------------------------------------------------------------------------------


# Main Entry Point
if __name__ == "__main__":

    # Needed Variables
    current_date = str(datetime.date.today().strftime("%Y-%m-%d")).split(" ")[0]
    data_path = r"V:\pln\Urbandesign\GRAPHICS\G&V_Citywide\Submission_QC\Data\WeeklyApplicationsLists"
    export_folder = r"V:\pln\Urbandesign\GRAPHICS\G&V_Citywide\Submission_QC\Data\MasterOutputs"
    masterfile_export = r"C:\Users\rmatade\Desktop\MasterQC_Backup\\"


    # Gather Data & Write Master File
    all_data = gather_data(data_path, export_folder)
    m_path = masterfile_export + current_date + "_MasterCSV.csv"
    all_data.to_csv(m_path, index = False)


    # With Master Data Split Into Districts & Format Excel Files
    export_data(all_data, export_folder, current_date)
