# Name:                                            Renacin Matadeen
# Date:                                               09/19/2021
# Title                             City Of Toronto Heritage Registry - Data QA (Tools)
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

        try:
            df = pd.read_csv(data_path)

        except PermissionError:
            print("Files Currently Open In Another Program")

        print(df.head())
