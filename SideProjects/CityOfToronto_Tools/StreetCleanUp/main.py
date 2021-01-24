# Name:                                            Renacin Matadeen
# Date:                                               01/19/2021
# Title                                  City Of Toronto Street Clean Up Tools
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
from tools import CoT_Tools
# ----------------------------------------------------------------------------------------------------------------------

def main():

    # Import Test DF & Run Through Created Tools
    df = pd.read_csv(r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\StreetCleanUp\Data\TestData.csv")

    # Make Sure Entries Are In Uppercase! | Then Clean Entries | Seperate Addresses | Modify Street Types
    df["StreetName"] = df["StreetName"].str.upper()
    df["StreetName"] = CoT_Tools.clean_entry(df["StreetName"])

    expanded_df = CoT_Tools.seperate_addresses(df, "StreetName")
    expanded_df["StreetName"] = CoT_Tools.full_street(expanded_df["StreetName"])
    expanded_df.to_csv(r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\StreetCleanUp\Data\CleanedTestData.csv", index=False)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
