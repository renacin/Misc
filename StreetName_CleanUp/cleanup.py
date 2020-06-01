# Name:                                            Renacin Matadeen
# Date:                                               05/28/2020
# Title                           Precursor To Street Cleaning Program - Understand The Data
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


# SECONDARY FUNCTION | Remove Direction If There
def remove_direction(street_text):

    # Street Abbreviations Stored Here | BE CAREFUL OF CANADIAN SPELLING | FOR TORONTO ONLY | BETTER AS JSON?
    street_dictionary = {
                        "ALLEY" : [" ALLEE ", " ALLEY ", " ALLY ", " ALY "],
                        "ANEX" : [" ANEX ", " ANNEX ", " ANNX ", " ANX "],
                        "AVENUE" : [" AV ", " AVE " , " AVEN " , " AVENU " , " AVENUE " , " AVN " , " AVNUE "],
                        "BOTTOM" : [" BOT ", " BTM ", " BOTTM "],
                        "BOULEVARD" : [" BLVD ", " BOUL ", " BOULV ", " BLVRD "],
                        "CENTRE" : [" CEN ", " CTR ", " CENT ", " CENTR ", " CENTR ", " CNTER ", " CNTR "],
                        "COMMON" : [" CMN "],
                        "CORNER" : [" COR "],
                        "COURSE" : [" CRSE "],
                        "COURT" : [" CRT ", " CT "],
                        "CREEK" : [" CRK "],
                        "CRESCENT" : [" CRES ", " CRSENT ", " CRSNT ", " CRSNT "],
                        "CROSSING" : [" CROSSING ", " XING ", " CRSSNG "],
                        "CIRCLE" : [" CRCL "],
                        "DRIVE" : [" DR ", " DRIV ", " DRV "],
                        "EXPRESSWAY" : [" EXP ", " EXPY ", " EXPR ", " EXPRESS ", " EXPW ", " EXPY "],
                        "GARDEN" : [" GDN ", " GARDN ", " GRDEN ", " GRDN "],
                        "GATE" : [" GT "],
                        "GATEWAY" : [" GTWY ", " GATEWY ", " GATWAY ", " GTWAY ", " GTWAY ", " GTWY "],
                        "HIGHWAY" : [" HWY ", " HIGHWY ", " HIWAY ", " HIWY ", " HWAY "],
                        "HILL" : [" HL "],
                        "JUNCTION" : [" JCT ", " JCTION ", " JUNCTN ", " JUNCTON "],
                        "LANE" : [" LN "],
                        "PARK" : [" PRK "],
                        "PARKWAY" : [" PARKWY ", " PKWAY ", " PKWY ", " PKY "],
                        "PATH" : [" PTH "],
                        "PLAZA" : [" PLZ ", " PLZA "],
                        "POINT" : [" PT "],
                        "RIVER" : [" RIV ", " RIVR ", " RVR "],
                        "ROAD" : [" RD "],
                        "ROUTE" : [" RTE "],
                        "SHORE" : [" SHOAR ", " SHR "],
                        "SQUARE" : [" SQ ", " SQR ", " SQRE ", " SQU "],
                        "STATION" : [" STA ", " STATN ", " STN "],
                        "STREET" : [" ST ", " STR ", " STRT "],
                        "TRAIL" : [" TRL "],
                        "TERRACE" : [" TER "],
                        "VILLE" : [" VL ", " VIL "],
                        "WAY" : [" WY "]
                        }

    # Prelim Conversions
    street_text = street_text.upper()
    street_text = str(street_text) + " "

    # Replace Direction To FullS
    for s_dir in list_dir:
        street_text = street_text.replace(s_dir, " ")

    street_text = street_text.replace("  ", " ")
    return street_text


# MAIN FUNCTION |
def main():

    # Column Of Focus
    street_name_col = "NAME"

    # Import The CSV File | Drop Duplicates
    raw_data = pd.read_csv(r"C:\Users\renac\Desktop\Misc\TorontoStreetData.csv")
    raw_data = raw_data.drop_duplicates(subset=[street_name_col])

    # Type Of Street Add To This List
    type_of_street = []

    # Remove West, East, North, or South
    for index, row in raw_data.iterrows():

        # Clean And Sepertate
        street_name = remove_direction(row[street_name_col])



# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
