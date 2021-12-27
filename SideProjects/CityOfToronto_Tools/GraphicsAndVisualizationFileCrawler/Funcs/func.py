# Name:                                            Renacin Matadeen
# Date:                                               10/31/2021
# Title           Interval House Data Analytics Project: Canadian Census Data K-Means Clustering Attempt
#
# ----------------------------------------------------------------------------------------------------------------------
import os, sys
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


class FileCrawler():
    """ This class stores all functions of this file crawler"""


    @staticmethod
    def filter_data(data_path: str, focus_variables: list) -> "Pandas Dataframe":
        """
        This class method imports the CSV file as a pandas dataframe and filters it
        based on the fields the user wants to focus on.
        """

        try:
            df_raw = pd.read_csv(data_path)
            df_filtered = df_raw.copy()
            df_filtered = df_filtered.fillna(0)

            if len(focus_variables) != 0:
                return df_filtered[focus_variables]

            return df_filtered

        except PermissionError:
            print("Files Currently Open In Another Program")
            raise PermissionError
