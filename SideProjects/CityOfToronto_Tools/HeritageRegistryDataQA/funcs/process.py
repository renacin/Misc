# Name:                                            Renacin Matadeen
# Date:                                               09/19/2021
# Title                             City Of Toronto Heritage Registry - Data QA (Tools)
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
# ----------------------------------------------------------------------------------------------------------------------


class ProcessData:
    """
    This class will store needed functions that will help identify common, and uncommon addresses between two datasets
    """

    # -----------------------------------------------------------------------------------------------------------------
    @staticmethod
    def filter_data(data_path):
        """ This function will identify key statistics from transit data | First explore the data"""
