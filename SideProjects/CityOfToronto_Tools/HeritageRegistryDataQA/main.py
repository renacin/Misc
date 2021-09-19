# Name:                                            Renacin Matadeen
# Date:                                               09/19/2021
# Title                                City Of Toronto Heritage Registry - Data QA
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
# ----------------------------------------------------------------------------------------------------------------------


class Dataset:
    """ Class used as method storage hub """

    @staticmethod
    def filter_data(data_path: str) -> "Pandas Dataframe":
        """ This function will ingest & filter needed columns only """

        # Try To Import Files, Be Mindful Of Alt Permissions
        try:
            df = pd.read_csv(data_path)

        except PermissionError:
            print("Files Currently Open In Another Program")

        # Only Keep Needed Columns
        columns_to_keep = ["PRSN", "ADDRESS"]
        df = df[columns_to_keep]

        return df


    @staticmethod
    def remove_dup(df: "Pandas Dataframe", dataframe_name: str) -> "Pandas Dataframe":
        """ This function will remove duplicates based on PRSN, keeping only primary addresses. This function prints statistics about the files """

        # Grab Dataframe Lenght Before & After
        df_len_before = len(df)
        df_after = df.drop_duplicates("PRSN", keep="first")
        rows_removed = df_len_before - len(df_after)

        # Return Num Of Addresses Removed
        print(f"LOGGING - {dataframe_name}, Start Lenght: {df_len_before} | Duplicates Removed: {rows_removed} | Rows Remaining: {df_len_before - rows_removed}")

        return df_after

# ----------------------------------------------------------------------------------------------------------------------


def main():
    """ Main logic of this python script. Import data, clean data, and then create comparison datasets from original
    data. Run if name equals main. """

    # Sources Of Data
    ibms_csv = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryDataQA\Data\DataFromIBMSTeam.csv"
    heritage_csv = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryDataQA\Data\DataFromHeritageTeam.csv"


    # Ingest & Filter Only Address & PRSN Column
    from_ibms_df = Dataset.filter_data(ibms_csv)
    from_heritage_df = Dataset.filter_data(heritage_csv)


    # Remove Duplicates From PRSN (Keep Only Primary Addresses)
    no_dup_ibms_df = Dataset.remove_dup(from_ibms_df, "IBMS Data")
    no_dup_heritage_df = Dataset.remove_dup(from_heritage_df, "Heritage Data")


    # Compare Both Datasets, Which Are Common, Which Can Only Be Found In Both


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
