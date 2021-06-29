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
	image_set = ImageSet()

	for folder_name in ["Folder_1", "Folder_2"]:
		image_set.ingest_images(f"C:/Users/renac/Desktop/TestImages/{folder_name}")

	# For Debugging
	print(image_set.file_ext_dict["FileExtensions"])

	# FILES IN FOLDER 1: 436, FILES IN FOLDER 2: 339, TOTAL 775

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()