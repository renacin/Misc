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
    TODO:
        + Tool That Removes (X) Count Of Rows In Entry

    """


    # Main Function That Seperates Entry That Is A Range Of Addresses
    def sep_addr_main(text):

        # Check To See If Address Is A Range Of Addresses [1000 - 1022]
        pattern_rangeofaddrs = r"\d+\s?[-]\s?\d+"
        rangeofaddrs = list(re.findall(pattern_rangeofaddrs, text))

        # If Entry Is A Range Of Addresses; Create A List Of Street Numbers | Else Returns The Street Address
        if (len(rangeofaddrs) != 0):

            for char_ in [" A ", " .5 ", " 0 ", "- ", "R"]:
                rangeofaddrs[0] = rangeofaddrs[0].replace(char_, "")
                rangeofaddrs[0] = rangeofaddrs[0].strip()

            range_values = rangeofaddrs[0].split("-")

            list_of_addresses = list(range(int(range_values[0]), int(range_values[1]) + 2, 2))

            if list_of_addresses[-1] != range_values[-1]:
                list_of_addresses = list(range(int(range_values[0]), int(range_values[1]) + 1, 1))

        else:
            pattern_addrs = r"\d+[.]?[0-9]?[A-Z]?"
            list_of_addresses = list(re.findall(pattern_addrs, text))

        # Return The Street Name From The Text | Do Final Clean Up
        streetname = text
        for addr in list_of_addresses:
            streetname = streetname.replace(str(addr), "")

        for char_ in [" - ", " -A "]:
            streetname = streetname.replace(char_, "")

        streetname = streetname.split(",")
        streetname_ = streetname[-1].replace("  ", "")

        return list_of_addresses, streetname_


    # [Function 1] Seperate Addresses Just In Case | Takes Entire DataFrame
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
            addresses, streetname = CoT_Tools.sep_addr_main(row[street_col])

            for addr in addresses:
                address = str(addr)

                if address[-1] != " ":
                    complete_street = address + " " + streetname
                else:
                    complete_street = address + streetname

                for char_ in [" - ", " -A ", "  ", "   "]:
                    complete_street = complete_street.replace(char_, " ")

                for col in col_names:
                    temp_dict[col].append(row[col])
                temp_dict[street_col].append(complete_street)

        return pd.DataFrame.from_dict(temp_dict)





    # ------------------------------------------------------------------------------------------------------------------






























# ----------------------------------------------------------------------------------------------------------------------


def main():

    # Import Test DF & Run Through Created Tools
    df = pd.read_csv(r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\StreetCleanUp\Data\TestData.csv")

    # Clean Streets With Class
    df_cleaned = CoT_Tools.seperate_addresses(df, "Street")

    df_cleaned.to_csv(r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\CityOfToronto_Tools\StreetCleanUp\Data\CleanedTestData.csv", index=False)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
