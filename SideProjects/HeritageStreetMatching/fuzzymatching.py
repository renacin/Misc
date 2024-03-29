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
    maindf = pd.read_csv(r"C:\Users\renac\Desktop\CityPatternsProject\Toronto_Schools_TCSB.csv")

    # Important Info Stored In This Column | Make Common Names!
    contrc_dates = "BUILT"
    col_street = "ADDRESS"

    # Fix Addresses In Parsed Data, Make It Easier For The Fuzz Match
    maindf = clean_df(maindf, col_street)
    secondarydf = clean_df(secondarydf, col_street)

    # Drop Unneeded Columns In Secondary DF | Loop Through Each Column Name
    for col_name in secondarydf.columns.tolist():
        if (col_name == contrc_dates) or (col_name == col_street):
            pass
        else:
            del secondarydf[col_name]

    # Merge Dataframes, Fuzzy Search Will Be Reserved For Rows That Haven't Been Matched CONCAT | MERGE
    merged_df = pd.merge(maindf, secondarydf)
    maindf_NaN = merged_df[merged_df[contrc_dates].isnull()]

    final_maindf = merged_df[~merged_df[contrc_dates].isnull()]

    # Loop through data in main df, try to find matching value in secondary
    matched_constructiondates = []
    matched_addr = []

    for index, row in maindf_NaN.iterrows():

        # Make The Column That Will Be Searched Against Smaller, Dont Compare The Entire DF - EXPENSIVE
        school_address_main = row[col_street] # Single Value

        # Comparison Terms | Row Value & New Comparison DF
        compval = str(row[col_street].split(" ")[1])

        filtered_df = secondarydf[secondarydf[col_street].str.contains(compval)]

        # Find An Appropriate Match
        fuzzymatch = process.extractOne(school_address_main, filtered_df[col_street], score_cutoff = 90)

        # Using Values Index, Return The Metric Of Focus
        try:
            build_date = secondarydf[contrc_dates][fuzzymatch[2]]
            matc_addr = fuzzymatch[0]

        except TypeError as e:
            build_date = ""
            matc_addr = ""

        matched_constructiondates.append(build_date)

    maindf_NaN["BUILT"] = matched_constructiondates
    final_secondarydf = maindf_NaN[~maindf_NaN[contrc_dates].isnull()]

    # Final Dataframe
    final_merged = pd.concat([final_maindf, final_secondarydf])

    # Write DF To CSV
    final_merged.to_csv(r"C:\Users\renac\Desktop\TCSB.csv", index=False)
    print("Finished Writting")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
