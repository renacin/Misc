# Name:                                            Renacin Matadeen
# Date:                                               09/19/2021
# Title                                City Of Toronto Heritage Registry - Data QA
#
# ----------------------------------------------------------------------------------------------------------------------
from funcs.process import *
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
