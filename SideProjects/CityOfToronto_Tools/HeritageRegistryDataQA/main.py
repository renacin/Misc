# Name:                                            Renacin Matadeen
# Date:                                               09/19/2021
# Title                                City Of Toronto Heritage Registry - Data QA
#
# ----------------------------------------------------------------------------------------------------------------------
from funcs.process import *
# ----------------------------------------------------------------------------------------------------------------------

def main():

    # Filter Only Address & PRSN Column

    try:
        ibms_csv = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryDataQA\Data\DataFromIBMSTeam.csv"
        heritage_csv = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\HeritageRegistryDataQA\Data\DataFromHeritageTeam.csv"
        
        from_ibms_df = pd.read_csv(ibms_csv)
        from_heritage_df = pd.read_csv(heritage_csv)

    except PermissionError:
        print("Files Currently Open In Another Program")




# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
