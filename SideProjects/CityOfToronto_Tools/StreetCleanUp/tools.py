# Name:                                            Renacin Matadeen
# Date:                                               01/19/2021
# Title                                  City Of Toronto Street Clean Up Tools
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import re
# ----------------------------------------------------------------------------------------------------------------------


class CoT_Tools:
    """
    This tool will aid in the Geolocation of User Inputed Address Points;
        Steps included:
            + Clean Entries Of User Errors
            + Expand Entries That Cover Multiple Addresses
            + Expand Street Types
    """


    # For [Function 1] Clean Addresses
    def _clean(entry):
        row_entry = entry.strip()
        bracket_pattern = r"\(.{1,20}\)"
        things2remove = list(re.findall(bracket_pattern, row_entry))

        for string2remove in things2remove:
            row_entry = row_entry.replace(string2remove, " ")

        for string2remove in ["  ", " R "]:
            row_entry = row_entry.replace(string2remove, " ")

        return row_entry


    # [Function 1] Remove Unneeded Characters
    @staticmethod
    def clean_entry(df_col):

        return [CoT_Tools._clean(x) for x in df_col]


    # ------------------------------------------------------------------------------------------------------------------


    # For [Function 2] Seperates Multiple Addresses
    def _sep_addr(text):

        # Check To See If Address Is A Range Of Addresses [1000 - 1022]
        text = str(text).strip()
        addr_range_pattern = r"\d+\s?[-]\s?\d+[.]?[A]?[5]?"
        range_of_addr = re.findall(addr_range_pattern, text)

        # Create A List Of Street Numbers | Else Returns The Street Address From The Original Text
        if (len(range_of_addr) != 0):

            # Split And Identify Special Addr Just Incase
            minmax_addrs = range_of_addr[0].strip().split("-")
            for index_num in range(len(minmax_addrs)):

                special_addr_pattern = r"\d+[A-Z]{1,2}"
                special_addr = re.findall(special_addr_pattern, minmax_addrs[index_num])

                if len(special_addr) != 0:
                    minmax_addrs[index_num] = minmax_addrs[index_num][:-1]

            # Both Are Even
            if (int(minmax_addrs[0]) % 2 == 0) and (int(minmax_addrs[1]) % 2 == 0):
                addresses = list(range(int(minmax_addrs[0]), int(minmax_addrs[1]) + 2, 2))

            # Both Are Odd
            elif (int(minmax_addrs[0]) % 2 != 0) and (int(minmax_addrs[1]) % 2 != 0):
                addresses = list(range(int(minmax_addrs[0]), int(minmax_addrs[1]) + 2, 2))

            # One Is Even & One Is Odd
            else:
                addresses = list(range(int(minmax_addrs[0]), int(minmax_addrs[1]) + 1, 1))

            # Add Special Addr Just Incase
            if len(special_addr) != 0:
                addresses.append(special_addr[0])

            # Find Addresses That Were Added With Range
            addr_pattern = r"\d+[.]?[0-9]?[A-Z]?"
            additional_addrs = re.findall(addr_pattern, text)
            addresses.extend(additional_addrs)

        else:
            addr_pattern = r"\d+[.]?[0-9]?[A-Z]?"
            addresses = re.findall(addr_pattern, text)

        # Final Addr Clean Up
        final_addr_list = list({str(x) for x in addresses})

        # Return The Street Name From The Text | Do Final Clean Up
        streetname = text.strip()
        for addr in final_addr_list:
            streetname = streetname.replace(str(addr), "")

        for char_ in [" - ", " -", "-", " -A ", " A ", " & "]:
            streetname = streetname.replace(char_, "")

        streetname = str(streetname).strip()
        streetname = streetname.split(",")
        streetname_ = streetname[-1].replace("  ", "")

        return final_addr_list, streetname_


    # [Function 2] Seperate Addresses Just In Case | Takes Entire DataFrame
    @staticmethod
    def seperate_addresses(df, street_col):

        # Place To Store Data
        temp_dict = {}
        for name in df.columns:
            temp_dict[name] = []

        # Iterate Through & Rewrite Data To New Dict
        col_names = [name for name in df.columns if name != street_col]

        # This Is O^3 YIKES
        for i, row in df.iterrows():
            addresses, streetname = CoT_Tools._sep_addr(row[street_col])

            for address in addresses:
                if ("A " == streetname[:2]):
                    streetname = streetname.replace("A ", " ")

                complete_street = str(address + " " + streetname).split()
                complete_street = " ".join(complete_street)

                for col in col_names:
                    temp_dict[col].append(row[col])
                temp_dict[street_col].append(complete_street)

        return pd.DataFrame.from_dict(temp_dict)


    # ------------------------------------------------------------------------------------------------------------------


    #  For [Function 3] Expand Street Direction
    def expand_dir(text):

        # Split By SpaceFor List Comp & Add Padding For Other Workflow
        street_as_list_dir = text.split(" ")
        street_dir_padding = " {} ".format(text)

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


    # For [Function 3] Gets String Ready For Next Steps
    def expand_prelim(text):

        # Add Padding
        padded_st_text = " {} ENDOFSEARCHLINE ".format(text)

        # Check To See If Text Entry Is Range Of Rows
        saint_designations = [" ST\.? "]
        dir_designations = ["NORTH", "EAST", "SOUTH", "WEST", "ENDOFSEARCHLINE"] # The + Indicated The End Of The Line

        # Pattern To Match
        saint_or_pattern = "|".join(saint_designations)
        dir_or_pattern = "|".join(dir_designations)

        saint_pattern = saint_or_pattern + "(?!" + dir_or_pattern + ")"
        st_expand = re.sub(saint_pattern, " SAINT ", padded_st_text)

        return st_expand[1:-17]


    #  For [Function 3] Expands Street Type
    def expand_str(street_text):

        full_st_type = ['ALLEY', 'ALLEY', 'ALLEY', 'ALLEY', 'ANEX', 'ANEX', 'ANEX', 'ANEX', 'AVENUE', 'AVENUE',
        'AVENUE', 'AVENUE', 'AVENUE', 'AVENUE', 'AVENUE', 'BOTTOM', 'BOTTOM', 'BOTTOM', 'BOULEVARD', 'BOULEVARD',
        'BOULEVARD', 'BOULEVARD', 'BOULEVARD', 'BRIDGE', 'CENTRE', 'CENTRE', 'CENTRE', 'CENTRE', 'CENTRE', 'CENTRE',
        'CENTRE', 'COMMON', 'CORNER', 'COURSE', 'COURT', 'COURT', 'CREEK', 'CRESCENT', 'CRESCENT', 'CRESCENT',
        'CRESCENT', 'CROSSING', 'CROSSING', 'CROSSING', 'CIRCLE','DRIVE', 'DRIVE', 'DRIVE', 'EXPRESSWAY',
        'EXPRESSWAY', 'EXPRESSWAY', 'EXPRESSWAY', 'EXPRESSWAY', 'EXPRESSWAY', 'GARDEN', 'GARDEN', 'GARDEN', 'GARDEN',
        'GARDENS', 'GATE', 'GROVE', 'GATEWAY', 'GATEWAY', 'GATEWAY', 'GATEWAY', 'GATEWAY', 'GATEWAY', 'HIGHWAY',
        'HIGHWAY', 'HIGHWAY', 'HIGHWAY', 'HIGHWAY', 'HILL', 'HEIGHTS', 'JUNCTION', 'JUNCTION', 'JUNCTION', 'JUNCTION',
        'LANE', 'LANE', 'LAWN', 'LINE', 'PARK', 'PARK', 'PARKWAY', 'PARKWAY', 'PARKWAY', 'PARKWAY', 'PATH', 'PLAZA',
        'PLAZA', 'PLACE', 'POINT', 'RIVER', 'RIVER', 'RIVER', 'ROAD', 'ROUTE', 'ROADWAY', 'ROADWAY', 'SHORE', 'SHORE',
        'SQUARE', 'SQUARE', 'SQUARE', 'SQUARE', 'STATION', 'STATION', 'STATION', 'STREET', 'STREET', 'STREET', 'TRAIL',
        'TERRACE', 'VILLE', 'VILLE', 'WAY', 'WOODS']

        abbrv_st_type = ['ALLEE', 'ALLEY', 'ALLY', 'ALY', 'ANEX', 'ANNEX', 'ANNX', 'ANX', 'AV', 'AVE', 'AVEN', 'AVENU',
        'AVENUE', 'AVN', 'AVNUE', 'BOT', 'BTM', 'BOTTM', 'BLVD', 'BOUL', 'BOULV', 'BLVRD', 'BV', 'BDGE', 'CEN', 'CTR',
        'CENT', 'CENTR', 'CENTR', 'CNTER', 'CNTR', 'CMN', 'COR', 'CRSE', 'CRT', 'CT', 'CR', 'CRES', 'CRSENT', 'CRSNT',
        'CRSNT', 'CROSSING', 'XING', 'CRSSNG', 'CRCL', 'DR', 'DRIV', 'DRV', 'EXP', 'EXPY', 'EXPR', 'EXPRESS', 'EXPW',
        'EXPY', 'GDN', 'GARDN', 'GRDEN', 'GRDN', 'GDNS', 'GT', 'GRV', 'GTWY', 'GATEWY', 'GATWAY', 'GTWAY', 'GTWAY',
        'GTWY', 'HWY', 'HIGHWY', 'HIWAY', 'HIWY', 'HWAY', 'HL', 'HTS', 'JCT', 'JCTION', 'JUNCTN', 'JUNCTON', 'LN',
        'Ln', 'LWN', 'LI', 'PRK', 'PK', 'PARKWY', 'PKWAY', 'PKWY', 'PKY', 'PTH', 'PLZ', 'PLZA', 'PL', 'PT', 'RIV',
        'RIVR', 'RVR', 'RD', 'RTE', 'ROADWAY', 'RDWY', 'SHOAR', 'SHR', 'SQ', 'SQR', 'SQRE', 'SQU', 'STA', 'STATN',
        'STN', 'ST', 'STR', 'STRT', 'TRL', 'TER', 'VL', 'VIL', 'WY', 'WDS']

        # Prelim Text Cleaning
        street_text_padding = " {} ".format(street_text)
        street_as_list = street_text.split(" ")

        # Look For Match And Query Match Type
        common_val = list(set(street_as_list) & set(abbrv_st_type))

        # Get Index, Find Associated Full Value & Replace
        for abbrv in common_val:
            full = full_st_type[abbrv_st_type.index(abbrv)]
            orginal_text = " {} ".format(abbrv)
            replace_text = " {} ".format(full)

            street_text_padding = street_text_padding.replace(orginal_text, replace_text)

        return street_text_padding[1:-1]


    # For [Function 3] Main Function That Packages Everything Together
    def full_street_setup(text):

        # Prelim Conversion
        text = text.upper()

        # Main Clean Up
        text_with_expanded_direction = CoT_Tools.expand_dir(text)
        text_with_prelim_setup = CoT_Tools.expand_prelim(text_with_expanded_direction)
        cleaned_text = CoT_Tools.expand_str(text_with_prelim_setup)

        # Final Conversion
        cleaned_text = cleaned_text.lower()
        cleaned_text = cleaned_text.title()

        # Fix 'S Issue
        cleaned_text = cleaned_text.replace("'S ", "'s ")

        # Return Value
        return cleaned_text


    # [Function 3] Preforms The Street
    @staticmethod
    def full_street(df_col):

        return [CoT_Tools.full_street_setup(x) for x in df_col]
