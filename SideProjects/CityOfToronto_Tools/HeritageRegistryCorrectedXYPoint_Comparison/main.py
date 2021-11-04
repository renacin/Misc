# Name:                                            Renacin Matadeen
# Date:                                               11/04/2021
# Title                  City Of Toronto Heritage Registry - Corrected & Inoperable X/Y Data Comparison
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------

def compare_datasets():
    """ This function compares both datasets """
    pass


# ----------------------------------------------------------------------------------------------------------------------
def main():
    """ Main logic of python file """
    # Sources Of Data
    good_xy = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryCorrectedXYPoint_Comparison\Data\Good_XY_Data.csv"
    bad_xy = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryCorrectedXYPoint_Comparison\Data\Bad_XY_Data.csv"

    df_good_xy = pd.read_csv(good_xy)
    df_bad_xy = pd.read_csv(bad_xy)

    # Read Both Sources Of Data
    print(df_good_xy.info())
    print(df_bad_xy.info())

    # Compare Both Sets Of Data
    compare_datasets()


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
