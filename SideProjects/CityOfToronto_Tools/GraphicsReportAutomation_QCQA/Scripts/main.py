# Name:                                            Renacin Matadeen
# Date:                                               01/07/2022
# Title                        City Of Toronto: Graphics & Visualization File Crawler
#
# ----------------------------------------------------------------------------------------------------------------------
import datetime
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


class QC_Checker:
    """ This class stores all functions of the Graphics & Visualization """

    # ------------------------------------------------------------------------------------------------------------------
    #   PRIVATE METHODS
    def __priv_func(self, var):
        """ Details """


    # ------------------------------------------------------------------------------------------------------------------
    #   PUBLIC METHODS
    def gather_data(self, data_path: str) -> "None":
        """
        Notes:
            Given the path of the folder that contains all XLSX documents that contain addresses passed through
            the graphics request FME automation script, combine all XLSX documents into one Pandas Dataframe.
            Dataframe cached as class static variable.
            applications.

        In:

        """


# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point
if __name__ == "__main__":

    # Main Logic Of Code
    qc_init = QC_Checker()
    qc_init.gather_data()
