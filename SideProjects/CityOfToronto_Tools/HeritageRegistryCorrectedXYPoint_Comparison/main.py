# Name:                                            Renacin Matadeen
# Date:                                               11/04/2021
# Title                  City Of Toronto Heritage Registry - Corrected & Inoperable X/Y Data Comparison
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------

def clean_datasets(df1_: "Pandas Dataframe", df2_: "Pandas Dataframe", focus_col: str, ) -> "Cleaned Pandas Dataframe":
    """ This function ensures both datasets have not only similar fields, but also similar datatypes & lenghts """

    def concat_string(detail):
        """ Internal function, used only to concat strings to 250 characters"""
        text_len = 250
        if len(str(detail)) > text_len:
            return detail[0:text_len]
        else:
            return detail

    # Make Shallow Copies Just In Case
    df1 = df1_.copy()
    df2 = df2_.copy()

    # Find Lenghts Of Strings
    good_xy_detail_maxlen = max([len(str(det)) for det in df1[focus_col].tolist()])
    bad_xy_detail_maxlen = max([len(str(det)) for det in df2[focus_col].tolist()])

    # If Max Lenght Is Equal, Return Both Datasets; Else Proceed With Data Cleaning
    if good_xy_detail_maxlen == bad_xy_detail_maxlen:
        return df1, df2

    # Concat Strings For Both Datasets
    df1[focus_col] = df1[focus_col].apply(lambda x: concat_string(str(x)))
    df2[focus_col] = df2[focus_col].apply(lambda x: concat_string(str(x)))

    # Print Max Comment Lenghts for Each Dataset
    print(df1.head())
    print(df2.head())


# ----------------------------------------------------------------------------------------------------------------------
def main():
    """ Main logic of python file """

    # Sources Of Data
    good_xy = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryCorrectedXYPoint_Comparison\Data\Good_XY_Data.csv"
    bad_xy = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryCorrectedXYPoint_Comparison\Data\Bad_XY_Data.csv"

    # Clean Both Datasets
    df_good_xy = pd.read_csv(good_xy)
    df_bad_xy = pd.read_csv(bad_xy)
    clean_datasets(df_good_xy[["Address", "Details"]], df_bad_xy[["Address", "Details"]], "Details")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
