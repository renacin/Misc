# Name:                                            Renacin Matadeen
# Date:                                               06/02/2020
# Title                                Dunctions Used To Clean Up Street Inputs
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import re
# ----------------------------------------------------------------------------------------------------------------------

"""
Notes:
    + Regular Expressions Are Extremely Important
        - Can Greatly Reduce Time Complexity In Most Cases, If Implemented Correctly

    + EXTENSION NOTATION:
        - saint_pattern = r"(?(" + '|'.join(string_lst) + r"))"
            +     '|'.join(string_lst) --> This Will Create A String Where The Values Are Glued Together By |
                                 (?= ) --> Matches if ... matches next, but doesn’t consume any of the string.
                                           This is called a lookahead assertion.
                                           Ex: Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.

        - saint_pattern = r"'|'.join(string_lst)(?!(" + '|'.join(dir_designations) + r"))"
            +     '|'.join(string_lst) --> This Will Create A String Where The Values Are Glued Together By |

"""

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

    # Final Touch-Ups | Remove Whitespace Infront
    if dir_expand[-1] == " ":
        dir_expand = dir_expand[:-1]

    return dir_expand






# SECONDARY FUNCTION | Expand Prelim Designations
def expand_prelim(street_text):
    # Unique End Of Line Designator
    endline_desig = "ENDOFSEARCHLINE"

    # Add Padding
    street_text = street_text.upper()
    padded_st_text = " " + street_text + " " + endline_desig + " "

    # Check To See If Text Entry Is Range Of Rows
    saint_designations = [" ST\.? "]
    dir_designations = ["NORTH", "EAST", "SOUTH", "WEST", endline_desig] # The + Indicated The End Of The Line

    # Pattern To Match
    saint_or_pattern = "|".join(saint_designations)
    dir_or_pattern = "|".join(dir_designations)

    saint_pattern = saint_or_pattern + "(?!" + dir_or_pattern + ")"
    st_expand = re.sub(saint_pattern, " SAINT ", padded_st_text)

    # Final Touch Ups
    st_expand = st_expand.replace(" " + endline_desig + " ", "")
    if st_expand[0] == " ":
        st_expand = st_expand[1:]

    return st_expand


# SECONDARY FUNCTION | Expand Street Type For Easier Comparison & Search | Pass List Of Full & Abbrv Street Types
def expand_str(street_text, str_full, str_abbrv):

    # Prelim Text Cleaning
    street_text_padding = " " + street_text + " "
    street_as_list = street_text.split(" ")

    # Look For Match And Query Match Type
    common_val = list(set(street_as_list) & set(str_abbrv))

    # Get Index, Find Associated Full Value
    full_list = []
    for val_ in common_val:
        abbrv_index = str_abbrv.index(val_)
        full_list.append(str_full[abbrv_index])

    # Replace Values In String
    for abbrv, full in zip(common_val, full_list):
        orginal_text = " " + abbrv + " "
        replace_text = " " + full + " "
        street_text_padding = street_text_padding.replace(orginal_text, replace_text)

    str_clean = street_text_padding[1:-1]

    return str_clean


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION | Clean Street Input
def main_clean(street_text, str_full, str_abbrv):


    dir_expanded = expand_dir(street_text)
    prelim_expanded = expand_prelim(dir_expanded)
    str_cleaned = expand_str(prelim_expanded, str_full, str_abbrv)

    return str_cleaned


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    pass
