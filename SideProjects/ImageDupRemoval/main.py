# Name:                                            Renacin Matadeen
# Date:                                               06/28/2021
# Title                                 Main Logic For Image Duplicate Removal
#
# ----------------------------------------------------------------------------------------------------------------------
from Functions.functions import *
# ----------------------------------------------------------------------------------------------------------------------


def main():
	""" The following function will store the main logic of this research project """

	# Instantiate Class
	image_set = ImageSet()

	# Ingest Images Keep Unique
	for folder_name in ["Folder_1", "Folder_2", "Folder_3", "Folder_4", "Folder_5", "Folder_6", "Folder_7"]:
		image_set.ingest_images(f"C:/Users/renac/Desktop/TestImages/{folder_name}")

	# Rewrite Unique Images Renaming Them With Date Taken Information
	image_set.rewrite_images("C:/Users/renac/Desktop/Pictures/")


def secondary():
	""" The following function will store secondary logic of this research project """
	
	ImageSet.rename_images("C:/Users/renac/Desktop/Pictures/2005_04_23_Alex3rdBirthday_VisitFromNewYorkFamily_B")


# ----------------------------------------------------------------------------------------------------------------------
# Main Entry Point Into Python Code
if __name__ == "__main__":

	# Run The Following Logic
    secondary()