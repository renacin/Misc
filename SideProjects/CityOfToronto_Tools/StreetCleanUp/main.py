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

    # Make Sure Entries Are In Uppercase!
    df["StreetName"] = df["StreetName"].str.upper()

    # Clean Streets With CoT_Tools.clean_entry
    df["StreetName"] = CoT_Tools.clean_entry(df["StreetName"])

    # Expand Rows With Multiple Addresses With
    CoT_Tools.seperate_addresses(df, "StreetName")

    # df.to_csv(r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\StreetCleanUp\Data\CleanedTestData.csv", index=False)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
