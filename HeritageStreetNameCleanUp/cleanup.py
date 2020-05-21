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
    # Check To See If Text Entry Is Range Of Rows
    pattern_rangeofaddrs = r"\d+\s?[-]\s?\d+"
    rangeofaddrs = list(re.findall(pattern_rangeofaddrs, text))

    # If Text Is A Range Create list_of_addresses Based On It
    if (len(rangeofaddrs) != 0):
        range_values = rangeofaddrs[0].split("-")
        min_val = int(range_values[0])
        max_val = int(range_values[1])
        list_of_addresses = list(range(min_val, max_val + 2, 2))

    # Else Do Usual Thing | Returns String Of Digits, With Possibly An Alphabetic Character
    else:
        pattern_addrs = r"\d+[.]?[0-9]?[A-Z]?"
        list_of_addresses = list(re.findall(pattern_addrs, text))

    # Return Just The Street Name
    streetname = text
    for addr in list_of_addresses:
        streetname = streetname.replace(str(addr), "")

    # Catch Leftover Bits, Remove Becareful Though
    streetname = streetname.replace(" A ", "")
    streetname = streetname.replace(" .5 ", "")
    streetname = streetname.replace(" 0 ", "")
    streetname = streetname.replace("- ", "")

    streetname = streetname.split(",")
    streetname_ = streetname[-1].replace("  ", "")

    return list_of_addresses, streetname_


# MAIN FUNCTION | Clean Up Heritage Data
def main():

    # Name Of Street Column
    streetcol = "Street"

    # Import CSV
    heritage_df = pd.read_csv(r"C:\Users\renac\Desktop\Heritage\HeritageNominations_C.csv")

    # Get Column Names As List
    col_names = [col for col in heritage_df.columns]

    # Create A Data Dictionary To Store Cleaned Results
    cleaned_data = {}
    for col in col_names:
        cleaned_data[col] = []

    # Loop Through Each Row
    for index, row in heritage_df.iterrows():

        # How Many Streets?
        list_of_addresses, streetname = addr_in_street_row(row[streetcol])


        # If 1 Address Just Append To Data, Else Iterate Through & Create Individual Addresses
        if (len(list_of_addresses) == 1):
            for col in col_names:
                cleaned_data[col].append(row[col])

        else:
            for addr_ in list_of_addresses:

                # Grab Full Addr
                full_addr = (str(addr_) + " " + streetname.upper())
                full_addr = full_addr.replace("  ", " ")

                # Append Data For Each New Addr
                for col in col_names:
                    if (col == streetcol):
                        cleaned_data[col].append(full_addr)

                    else:
                        cleaned_data[col].append(row[col])

    # Dictionary To Dataframe
    final_df = pd.DataFrame.from_dict(cleaned_data)
    final_df.to_csv(r"C:\Users\renac\Desktop\Heritage\HeritageNominations_Cleaned.csv", index=False)
    print("Finished Writting")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
