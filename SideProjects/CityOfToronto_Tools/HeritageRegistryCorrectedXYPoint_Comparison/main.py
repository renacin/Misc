# Name:                                            Renacin Matadeen
# Date:                                               11/04/2021
# Title                  City Of Toronto Heritage Registry - Corrected & Inoperable X/Y Data Comparison
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------
class Dataset:
    """ Class used as method storage hub """

    @staticmethod
    def compare_data(df1: "Pandas Dataframe", df1_name: str, df2: "Pandas Dataframe", df2_name: str) -> "Multiple CSVs":
        """ Compare Both Datasets & Return Counts Of Common, Uncommon Rows. Outputs CSVs Will Be Written """

        # Merge Datasets
        combined_df = df1.merge(df2, on="PRSN", how="outer", indicator=True)

        # Change Column Names, Change Merge Values To Better Represent Origin
        mapset = {"left_only": df1_name, "right_only": df2_name, "both": "Both Datasets"}
        combined_df.replace({"_merge": mapset}, inplace=True)
        combined_df.drop(["ADDRESS_y"], axis=1, inplace=True)
        combined_df.rename(columns = {"ADDRESS_x": "ADDRESS", "_merge": "Dataset Origin"}, inplace = True)

        # Report Number Of Common Rows, Uncommon Rows For Each Dataset
        for origin in mapset.values():
            filtered_df = combined_df[combined_df["Dataset Origin"] == origin]
            print(f"REPORT - Unique Rows Found In {origin}: {len(filtered_df)}")

        # Export Data As CSV
        combined_df.to_csv(r"C:\Users\renac\Desktop\Comparison_Dataset.csv", index=False)


# ----------------------------------------------------------------------------------------------------------------------
def main():
    """ Main logic of this python script. Import data, clean data, and then create comparison datasets from original
    data. Run if name equals main. """

    # Sources Of Data
    good_xy = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryDataQA\Data\DataFromIBMSTeam.csv"
    bad_xy = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryDataQA\Data\DataFromHeritageTeam.csv"

    # Read Both Sources Of Data


    # # Compare Both Datasets, Which Are Common, Which Can Only Be Found In Both
    # Dataset.compare_data(no_dup_ibms_df, "IBMS Data", no_dup_heritage_df, "Heritage Data")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
