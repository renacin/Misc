# Name:                                            Renacin Matadeen
# Date:                                               06/02/2020
# Title                                Dunctions Used To Clean Up Street Inputs
#
# ----------------------------------------------------------------------------------------------------------------------


# SECONDARY FUNCTION | Expand Prelim Designations
def expand_prelim(street_text):

    print(street_text)














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

    # For Each Entry In The Dictionary Try To Replace | Len Of Original Metric Either Cont/End
    orig_len = len(street_text_edge)
    for key_, value_ in dir_dictionary.items():

        # Try To Replace
        str_repl = " " + str(value_[0]) + " "
        key_repl = " " + str(key_) + " "
        dir_expand = street_text_edge.replace(str_repl, key_repl)

        # Always Loop Through All Directions Edge Cases That Contain More Than One
        if len(dir_expand) > orig_len:
            street_text_edge = dir_expand

    return dir_expand


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
                        "CREEK" : ["CR"],
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
                        "LINE" : ["LI"],
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
    street_text_edge = " " + street_text + " "


    # For Each Entry In The Dictionary Compare And Exand The Street Type | Set Default Just Incase
    str_expand = street_text
    orig_len = len(str_expand)
    for key_, value_ in street_dictionary.items():

        # Look For Match And Query Match Type
        common_val = list(set(street_as_list) & set(value_))

        if len(common_val) > 0:

            str_repl = " " + common_val[0] + " "
            key_repl = " " + key_ + " "
            str_expand = street_text_edge.replace(str_repl, key_repl)

            # Always Loop Through All Directions Edge Cases That Contain More Than One
            if len(str_expand) > orig_len:
                street_text_edge = str_expand

    # Final Touch-Ups | Remove Whitespace Infront
    if str_expand[0] == " ":
        str_expand = str_expand[1:]

    return str_expand


# MAIN FUNCTION | Clean Street Input
def main_clean(street_text):

    prelim_expanded = expand_prelim(street_text)

    # dir_expanded = expand_dir(street_text)
    # str_cleaned = expand_str(dir_expanded)
    #
    # return 1


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass