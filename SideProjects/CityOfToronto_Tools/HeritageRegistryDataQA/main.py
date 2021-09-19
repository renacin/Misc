# Name:                                            Renacin Matadeen
# Date:                                               09/19/2021
# Title                                City Of Toronto Heritage Registry - Data QA
#
# ----------------------------------------------------------------------------------------------------------------------
from funcs.process import *
# ----------------------------------------------------------------------------------------------------------------------

def main():

    # Sources Of Data
    ibms_csv = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryDataQA\Data\DataFromIBMSTeam.csv"
    heritage_csv = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryDataQA\Data\DataFromHeritageTeam.csv"

    # Ingest & Filter Only Address & PRSN Column
    from_ibms_df = Dataset.filter_data(ibms_csv)
    from_heritage_df = Dataset.filter_data(heritage_csv)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
