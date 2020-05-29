# Name:                                            Renacin Matadeen
# Date:                                               05/28/2020
# Title                           Precursor To Street Cleaning Program - Understand The Data
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


# SECONDARY FUNCTION | Remove Direction If There
def remove_direction(street_text):

    # Convert, Just Incase Spelt Version Is Also There
    list_dir = [" N ", " E ", " S ", " W ", " NORTH ", " EAST ", " SOUTH ", " WEST "]

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
        street_vars = street_name.split(" ")

        # Be Careful Of Empty Strings
        if (len(street_vars[-1]) == 0):
            street_type = street_vars[-2]
        else:
            street_type = street_vars[-1]

        # Append Data
        if street_type not in type_of_street:
            type_of_street.append(street_type)

    file = open(r"C:\Users\renac\Desktop\Misc\StreetTypeData.csv", "w")
    file.write(str(type_of_street))
    file.close()


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
