# Name:                                            Renacin Matadeen
# Date:                                               05/28/2020
# Title                           Precursor To Street Cleaning Program - Understand The Data
#
# ----------------------------------------------------------------------------------------------------------------------
from Functions_Dir.cln_func import *
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


def main():

    # Column Of Focus
    street_name_col = "NAME"

    # Import The CSV File | Drop Duplicates
    raw_data = pd.read_csv(r"C:\Users\renac\Desktop\Misc\TorontoStreetData.csv")
    raw_data = raw_data.drop_duplicates(subset=[street_name_col])

    # Type Of Street Add To This List
    type_of_street = []

    # For Debugging
    data_dictionary = {"Raw_Address": [], "Cleaned_Address": []}

    # Remove West, East, North, or South
    for index, row in raw_data.iterrows():

        # Clean Street Inputs
        cln_str = main_clean(row[street_name_col])
        
        data_dictionary["Raw_Address"].append(row[street_name_col])
        data_dictionary["Cleaned_Address"].append(cln_str)

    # DEBUGGING
    final_df = pd.DataFrame.from_dict(data_dictionary)
    final_df.to_csv(r"C:\Users\renac\Desktop\Test.csv", index=False)
    print("Finished Writting")

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
