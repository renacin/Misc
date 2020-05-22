# Name:                                            Renacin Matadeen
# Date:                                               05/19/2020
# Title                                          HeritageStreetNameCleanUp
#
# ----------------------------------------------------------------------------------------------------------------------
from fuzzywuzzy import process, fuzz
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


# SECONDARY FUNCTION | Full Street Name
def clean_addr(addr):

    # Convert To Upper | Upper doesn't help with fuzzy match, but helps with street type conversion
    address_ = addr.upper()

    # Replace Concat Street Types
    street_concat = {" ST ": "STREET ", " AVE ":" AVENUE ",
                     " LN ":" LANE ",
                     " TRL ":" TRAIL ",
                     " DR ":"DRIVE",
                     " CRES ":" CRESCENT ",
                     " BLVD ":" BOULEVARD ",
                     " RD ":" ROAD ",
                     " TER ":" TERRACE ",
                     " SQ ":" SQUARE ",
                     " GT ":" GATE ",
                     " PKWY ":" PARKWAY ",
                     " CRCL ":" CIRCLE "}

    # Prelim Clean Up
    addr_raw = str(address_) + " "
    addr_raw = addr_raw.replace(" W ", "WEST")
    addr_raw = addr_raw.replace(" E ", "EAST")
    addr_raw = addr_raw.replace(" N ", "NORTH")
    addr_raw = addr_raw.replace(" S ", "SOUTH")
    addr_raw = addr_raw.replace("  ", " ")

    for key, value in street_concat.items():
        addr_raw = addr_raw.replace(key, value)

    return addr_raw


# MAIN FUNCTION | Clean Up Heritage Data
def main():

    # Import CSVs
    tdsb_schools_df = pd.read_csv(r"C:\Users\renac\Desktop\CityPatternsProject\Toronto_Schools_TDSB.csv")
    schools_construction_df = pd.read_csv(r"C:\Users\renac\Desktop\CityPatternsProject\Toronto_Schools_ConstructionDates.csv")

    # Fix Addresses In Parsed Data, Make It Easier For The Fuzz Match
    cleaned_addrs = []
    for index, row in schools_construction_df.iterrows():
        cleaned_addrs.append(clean_addr(row["ADDRESS"]))
    
    schools_construction_df["ADDRESS"] = cleaned_addrs
    print(schools_construction_df.head())

    # # Dictionary To Dataframe
    # final_df = pd.DataFrame.from_dict(cleaned_data)
    # final_df.to_csv(r"C:\Users\renac\Desktop\Heritage\HeritageNominations_Cleaned.csv", index=False)
    # print("Finished Writting")



# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
