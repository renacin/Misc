# Name:                                            Renacin Matadeen
# Date:                                               06/28/2021
# Title                                 Main Logic For Image Duplicate Removal
#
# ----------------------------------------------------------------------------------------------------------------------
from Functions.functions import *
# ----------------------------------------------------------------------------------------------------------------------


""" The following function will store the main logic of this research project """
def main():

	# Instantiate Class Pointing To Main Folder
	folder_path = r"C:/Users/renac/Desktop/TestImages/Folder_1"
	image_set = ImageSet()
	image_set.ingest_images(folder_path)


# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()