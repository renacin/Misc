# Name:                                            Renacin Matadeen
# Date:                                               06/02/2020
# Title                                Dunctions Used To Clean Up Street Inputs
#
# ----------------------------------------------------------------------------------------------------------------------


# SECONDARY FUNCTION | Expand Street Direction
def expand_dir(street_text):

    # Comparison Dictionary
    dir_dictionary = {
                        "NORTH" : ["N"],
                        "EAST" : ["E"],
                        "SOUTH" : ["S"],
                        "WEST" : ["W"]
                    }

    # Prelim Text Cleaning
    street_text = street_text.upper()
    street_as_list = street_text.split(" ")
    street_text_edge = street_text + " "

    # For Each Entry In The Dictionary Try To Replace
    for key_, value_ in dir_dictionary.items():

        # Try To Replace
        str_repl = " " + str(value_[0]) + " "
        key_repl = " " + str(key_) + " "
        dir_expand = street_text_edge.replace(str_repl, key_repl)

        # If Value Expanded break out Of Loop
        if len(dir_expand) > len(street_text_edge):
            break

    return_val = str(dir_expand)
    return return_val


# SECONDARY FUNCTION | Expand Street Type For Easier Comparison & Search
def expand_str(street_text):

    # Street Abbreviations Stored Here | BE CAREFUL OF CANADIAN SPELLING | FOR TORONTO ONLY | BETTER AS JSON?
    street_dictionary = {
                        "ALLEY" : ["ALLEE", "ALLEY", "ALLY", "ALY"],
                        "ANEX" : ["ANEX", "ANNEX", "ANNX", "ANX"],
                        "AVENUE" : ["AV", "AVE" , "AVEN" , "AVENU" , "AVENUE" , "AVN" , "AVNUE"],
                        "BOTTOM" : ["BOT", "BTM", "BOTTM"],
                        "BOULEVARD" : ["BLVD", "BOUL", "BOULV", "BLVRD"],
                        "CENTRE" : ["CEN", "CTR", "CENT", "CENTR", "CENTR", "CNTER", "CNTR"],
                        "COMMON" : ["CMN"],
                        "CORNER" : ["COR"],
                        "COURSE" : ["CRSE"],
                        "COURT" : ["CRT", "CT"],
                        "CREEK" : ["CRK"],
                        "CRESCENT" : ["CRES", "CRSENT", "CRSNT", "CRSNT"],
                        "CROSSING" : ["CROSSING", "XING", "CRSSNG"],
                        "CIRCLE" : ["CRCL"],
                        "DRIVE" : ["DR", "DRIV", "DRV"],
                        "EXPRESSWAY" : ["EXP", "EXPY", "EXPR", "EXPRESS", "EXPW", "EXPY"],
                        "GARDEN" : ["GDN", "GARDN", "GRDEN", "GRDN"],
                        "GARDENS" : ["GDNS"],
                        "GATE" : ["GT"],
                        "GROVE" : ["GRV"],
                        "GATEWAY" : ["GTWY", "GATEWY", "GATWAY", "GTWAY", "GTWAY", "GTWY"],
                        "HIGHWAY" : ["HWY", "HIGHWY", "HIWAY", "HIWY", "HWAY"],
                        "HILL" : ["HL"],
                        "HEIGHTS" : ["HTS"],
                        "JUNCTION" : ["JCT", "JCTION", "JUNCTN", "JUNCTON"],
                        "LANE" : ["LN", "Ln"],
                        "LAWN" : ["LWN"],
                        "PARK" : ["PRK", "PK"],
                        "PARKWAY" : ["PARKWY", "PKWAY", "PKWY", "PKY"],
                        "PATH" : ["PTH"],
                        "PLAZA" : ["PLZ", "PLZA"],
                        "PLACE" : ["PL"],
                        "POINT" : ["PT"],
                        "RIVER" : ["RIV", "RIVR", "RVR"],
                        "ROAD" : ["RD"],
                        "ROUTE" : ["RTE"],
                        "ROADWAY" : ["ROADWAY", "RDWY"],
                        "SHORE" : ["SHOAR", "SHR"],
                        "SQUARE" : ["SQ", "SQR", "SQRE", "SQU"],
                        "STATION" : ["STA", "STATN", "STN"],
                        "STREET" : ["ST", "STR", "STRT"],
                        "TRAIL" : ["TRL"],
                        "TERRACE" : ["TER"],
                        "VILLE" : ["VL", "VIL"],
                        "WAY" : ["WY"],
                        "WOODS" : ["WDS"]
                        }

    # Prelim Text Cleaning
    street_text = street_text.upper()
    street_as_list = street_text.split(" ")
    street_text_edge = street_text + " "


    # For Each Entry In The Dictionary Compare And Exand The Street Type | Set Default Just Incase
    str_expand = street_text
    for key_, value_ in street_dictionary.items():

        # Look For Match And Query Match Type
        common_val = list(set(street_as_list) & set(value_))

        if len(common_val) > 0:
            str_repl = " " + common_val[0] + " "
            key_repl = " " + key_ + " "
            str_expand = street_text_edge.replace(str_repl, key_repl)
            break

    return str_expand


# MAIN FUNCTION | Clean Street Input
def main_clean(street_text):

    dir_expanded = expand_dir(street_text)
    str_cleaned = expand_str(dir_expanded)

    return str_cleaned


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
