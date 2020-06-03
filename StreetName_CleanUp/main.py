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

    # Remove West, East, North, or South
    for index, row in raw_data.iterrows():

        # Clean And Sepertate
        cln_street = expand_clean(row[street_name_col])
        print(cln_street)



# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
