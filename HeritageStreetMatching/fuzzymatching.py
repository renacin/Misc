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
    street_concat = {" ST ": " STREET ", " AVE ":" AVENUE ", " LN ":" LANE ", " TRL ":" TRAIL ",
                     " DR ":" DRIVE", " CRES ":" CRESCENT ", " BLVD ":" BOULEVARD ", " RD ":" ROAD ",
                     " TER ":" TERRACE ", " SQ ":" SQUARE ", " GT ":" GATE ", " PKWY ":" PARKWAY ",
                     " CRCL ":" CIRCLE "}

    # Prelim Clean Up
    addr_raw = str(address_) + " "
    addr_raw = addr_raw.replace(" W ", " WEST")
    addr_raw = addr_raw.replace(" E ", " EAST")
    addr_raw = addr_raw.replace(" N ", " NORTH")
    addr_raw = addr_raw.replace(" S ", " SOUTH")
    addr_raw = addr_raw.replace("  ", " ")

    for key, value in street_concat.items():
        addr_raw = addr_raw.replace(key, value)

    return addr_raw


# SECONDARY FUNCTION | Clean DFs
def clean_df(df, col_name_):
    cleaned_addrs = []

    for index, row in df.iterrows():
        cleaned_addrs.append(clean_addr(row[col_name_]))

    df[col_name_] = cleaned_addrs

    return df


# MAIN FUNCTION | Clean Up Heritage Data
def main():

    # Import CSVs
    secondarydf = pd.read_csv(r"C:\Users\renac\Desktop\CityPatternsProject\Toronto_Schools_ConstructionDates.csv")
    maindf = pd.read_csv(r"C:\Users\renac\Desktop\CityPatternsProject\Toronto_Schools_TDSB.csv")

    # Important Info Stored In This Column | Make Common Names!
    contrc_dates = "BUILT"
    col_street = "ADDRESS"

    # Fix Addresses In Parsed Data, Make It Easier For The Fuzz Match
    cln_secondarydf = clean_df(secondarydf, col_street)
    cln_maindf = clean_df(maindf, col_street)

    # Loop through data in main df, try to find matching value in secondary
    matched_constructiondates = []
    matched_addr = []

    for index, row in cln_maindf.iterrows():
        school_address = row[col_street]
        fuzzymatch = process.extractOne(school_address, cln_secondarydf[col_street], score_cutoff = 90)

        # Using Values Index, Return The Metric Of Focus
        try:
            build_date = cln_secondarydf[contrc_dates][fuzzymatch[2]]
            matc_addr = fuzzymatch[0]

        except TypeError as e:
            build_date = ""
            matc_addr = ""

        matched_constructiondates.append(build_date)
        matched_addr.append(matc_addr)

    cln_maindf["BUILT_DATE"] = matched_constructiondates
    cln_maindf["MATCH_ADDR"] = matched_addr

    # Write DF To CSV
    cln_maindf.to_csv(r"C:\Users\renac\Desktop\CityPatternsProject\TDSB_ContructDates.csv", index=False)
    print("Finished Writting")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
