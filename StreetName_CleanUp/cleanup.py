# Name:                                            Renacin Matadeen
# Date:                                               05/19/2020
# Title                                          HeritageStreetNameCleanUp
#
# ----------------------------------------------------------------------------------------------------------------------
from fuzzywuzzy import process, fuzz
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


# SECONDARY FUNCTION | Full Street Name
def clean_addr(addr):

    # Convert To Upper | Upper doesn't help with fuzzy match, but helps with street type conversion
    address_ = addr.upper()

    # Replace Concat Street Types
    street_concat = {" ST ": " STREET ", " AVE ":" AVENUE ", " LN ":" LANE ", " TRL ":" TRAIL ",
                     " DR ":" DRIVE", " CRES ":" CRESCENT ", " BLVD ":" BOULEVARD ", " RD ":" ROAD ",
                     " TER ":" TERRACE ", " SQ ":" SQUARE ", " GT ":" GATE ", " PKWY ":" PARKWAY ",
                     " CRCL ":" CIRCLE "}

    # Prelim Clean Up
    addr_raw = str(address_) + " "
    addr_raw = addr_raw.replace(" W ", " WEST")
    addr_raw = addr_raw.replace(" E ", " EAST")
    addr_raw = addr_raw.replace(" N ", " NORTH")
    addr_raw = addr_raw.replace(" S ", " SOUTH")
    addr_raw = addr_raw.replace("  ", " ")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
