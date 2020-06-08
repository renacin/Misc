# Name:                                            Renacin Matadeen
# Date:                                               06/02/2020
# Title                                Dunctions Used To Clean Up Street Inputs
#
# ----------------------------------------------------------------------------------------------------------------------
import re
# ----------------------------------------------------------------------------------------------------------------------


# SECONDARY FUNCTION | Expand Street Direction
def expand_dir(street_text):

    # Prelim Text Cleaning
    street_as_list_dir = street_text.split(" ")
    street_dir_padding = " {} ".format(street_text)

    # Comparison Dictionary
    dir_abbr = ["N", "E", "S", "W"]
    dir_full = ["NORTH", "EAST", "SOUTH", "WEST"]

    # Find Values To Replace
    common_dir = list(set(street_as_list_dir) & set(dir_abbr))

    for abbrv_dir in common_dir:
        full_direction = dir_full[dir_abbr.index(abbrv_dir)]
        orginal_dir = " {} ".format(abbrv_dir)
        replace_dir = " {} ".format(full_direction)
        street_dir_padding = street_dir_padding.replace(orginal_dir, replace_dir)

    return street_dir_padding[1:-1]


# SECONDARY FUNCTION | Expand Prelim Designations
def expand_prelim(street_text):

    # Add Padding
    padded_st_text = " {} ENDOFSEARCHLINE ".format(street_text)

    # Check To See If Text Entry Is Range Of Rows
    saint_designations = [" ST\.? "]
    dir_designations = ["NORTH", "EAST", "SOUTH", "WEST", "ENDOFSEARCHLINE"] # The + Indicated The End Of The Line

    # Pattern To Match
    saint_or_pattern = "|".join(saint_designations)
    dir_or_pattern = "|".join(dir_designations)

    saint_pattern = saint_or_pattern + "(?!" + dir_or_pattern + ")"
    st_expand = re.sub(saint_pattern, " SAINT ", padded_st_text)

    return st_expand[1:-17]


# SECONDARY FUNCTION | Expand Street Type For Easier Comparison & Search | Pass List Of Full & Abbrv Street Types
def expand_str(street_text, str_full, str_abbrv):

    # Prelim Text Cleaning
    street_text_padding = " {} ".format(street_text)
    street_as_list = street_text.split(" ")

    # Look For Match And Query Match Type
    common_val = list(set(street_as_list) & set(str_abbrv))

    # Get Index, Find Associated Full Value & Replace
    for abbrv in common_val:
        full = str_full[str_abbrv.index(abbrv)]
        orginal_text = " {} ".format(abbrv)
        replace_text = " {} ".format(full)

        street_text_padding = street_text_padding.replace(orginal_text, replace_text)

    return street_text_padding[1:-1]


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION | Clean Street Input
def combined_clean(street_text, str_full, str_abbrv):

    # Prelim Conversion
    street_text = street_text.upper()

    # Main Clean Up
    dir_expanded = expand_dir(street_text)
    prelim_expanded = expand_prelim(dir_expanded)
    str_cleaned = expand_str(prelim_expanded, str_full, str_abbrv)

    # Return Value
    return str_cleaned


# MAIN FUNCTION | Implementation For Multiprocessing Attempt
def main_function(street_list, str_full, str_abbrv, processor_id, return_data):

    # Compute Data & Return Data To Manager
    cleaned_data = [combined_clean(x, str_full, str_abbrv) for x in street_list]
    return_data["Processor" + str(processor_id)] = cleaned_data

# ----------------------------------------------------------------------------------------------------------------------
