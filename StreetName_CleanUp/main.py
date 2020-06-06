# Name:                                            Renacin Matadeen
# Date:                                               05/28/2020
# Title                           Precursor To Street Cleaning Program - Understand The Data
#
# ----------------------------------------------------------------------------------------------------------------------
from Functions_Dir.cln_func import *
import pandas as pd
import time
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

    # Use List Comprehension To Create Another List
    cln_addr = [main_clean(x, str_full_list, str_abbrv_list) for x in raw_data[street_name_col]]

    # DEBUGGING
    raw_data["Cleaned_ADDR"] = cln_addr
    raw_data.to_csv(r"C:\Users\renac\Desktop\Test.csv", index=False)
    print("Finished Writting")


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()


#
