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

	# Ingest Images Keep Unique
	for folder_name in ["Folder_1", "Folder_2"]:
		image_set.ingest_images(f"C:/Users/renac/Desktop/TestImages/{folder_name}")

	# Rewrite Unique Images Renaming Them With Date Taken Information
	image_set.rewrite_images("C:/Users/renac/Desktop/TestImages/")


	# F1: 436, F2: 339, TOTAL 775

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()