# Name:                                            Renacin Matadeen
# Date:                                               05/19/2020
# Title                                          HeritageStreetNameCleanUp
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import re
# ----------------------------------------------------------------------------------------------------------------------


# SECONDARY FUNCTION | Determine How Many Addresses In The Street Row
def addr_in_street_row(text):

    #Returns String Of Digits, With Possibly An Alphabetic Character
    pattern = r"\d+[A-Z]?"
    list_of_addresses = re.findall(pattern, text)

    # Return Just The Street Name
    streetname = text
    for addr in list_of_addresses:
        streetname = streetname.replace(addr, "")

    return list_of_addresses, streetname


# MAIN FUNCTION | Clean Up Heritage Data
def main():
    # List Of Column Name
    col_names = ["AssociatedProject", "Street","NumberOfAddresses", "DateOfConstruction",
                "Typology", "Nominated_TF", "Nominated", "Decision", "Notes", "Status"]

    # Create Dictionary To Store Cleaned Results
    cleaned_data = {
                    "AssociatedProject": [],
                    "Street": [],
                    "NumberOfAddresses": [],
                    "DateOfConstruction": [],
                    "Typology": [],
                    "Nominated_TF": [],
                    "Nominated": [],
                    "Decision": [],
                    "Notes": [],
                    "Status": []
                   }

    # Import CSV
    heritage_df = pd.read_csv(r"C:\Users\renac\Desktop\Heritage\HeritageSites_C.csv")

    # Loop Through Each Row
    for index, row in heritage_df.iterrows():

        # How Many Streets?
        list_of_addresses, streetname = addr_in_street_row(row["Street"])

        # If 1 Address Just Append To Data, Else Iterate Through & Create Individual Addresses
        if (len(list_of_addresses) == 1):
            for col in col_names:
                cleaned_data[col].append(row[col])

        print(cleaned_data)
        break
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
