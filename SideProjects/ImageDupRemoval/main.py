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
	main_path = "E:/Pictures/Matadeen_Pictures"
	image_folder = os.listdir(main_path)

	for item in image_folder:
		full_path = f"{main_path}/{item}"

		if (os.path.isdir(full_path)) and (item not in ["0000_00_00_Untracked", "2021_03_25_StevenAndUmaWedding"]):
			print(f"Working On Folder: {item}")
			ImageSet.rename_images(full_path)


# ----------------------------------------------------------------------------------------------------------------------
# Main Entry Point Into Python Code
if __name__ == "__main__":

	# Run The Following Logic
    secondary()