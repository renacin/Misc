# Name:                                            Renacin Matadeen
# Date:                                               05/28/2020
# Title                           Precursor To Street Cleaning Program - Understand The Data
#
# ----------------------------------------------------------------------------------------------------------------------
from Functions_Dir.cln_func import *
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION | Stores General Flow Of Program
def main():

    # Read Street Abbrv To Be Passed Into Function: expand_str
    str_abbrv = pd.read_csv(r"C:\Users\renac\Documents\Programming\Python\Misc\StreetName_CleanUp\Data\StreetAbbrv.csv")
    str_full_list = list(str_abbrv["Full"])
    str_abbrv_list = list(str_abbrv["Abbrv"])

    # Import The CSV File | Drop Duplicates
    street_name_col = "NAME"
    raw_data = pd.read_csv(r"C:\Users\renac\Desktop\Misc\TorontoStreetData.csv")
    raw_data = raw_data.drop_duplicates(subset=[street_name_col])

    # Final Data Dicitonary
    data_dictionary = {"Raw_Address": [], "Cleaned_Address": []}

    # Remove West, East, North, or South
    for index, row in raw_data.iterrows():

        # Clean Street Inputs
        street_text = row[street_name_col].upper()
        cln_str = main_clean(street_text, str_full_list, str_abbrv_list)

        data_dictionary["Raw_Address"].append(row[street_name_col])
        data_dictionary["Cleaned_Address"].append(cln_str)

    # DEBUGGING
    final_df = pd.DataFrame.from_dict(data_dictionary)
    final_df.to_csv(r"C:\Users\renac\Desktop\Test.csv", index=False)
    print("Finished Writting")


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
