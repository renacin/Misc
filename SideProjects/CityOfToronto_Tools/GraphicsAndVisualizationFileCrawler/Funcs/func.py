# Name:                                            Renacin Matadeen
# Date:                                               10/31/2021
# Title           Interval House Data Analytics Project: Canadian Census Data K-Means Clustering Attempt
#
# ----------------------------------------------------------------------------------------------------------------------
import os, sys
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


class FileCrawler():
    """ This class stores all functions of this file crawler"""


    @staticmethod
    def filter_data(data_path: str, focus_variables: list) -> "Pandas Dataframe":
        """
        This class method imports the CSV file as a pandas dataframe and filters it
        based on the fields the user wants to focus on.
        """

        try:
            df_raw = pd.read_csv(data_path)
            df_filtered = df_raw.copy()
            df_filtered = df_filtered.fillna(0)

            if len(focus_variables) != 0:
                return df_filtered[focus_variables]

            return df_filtered

        except PermissionError:
            print("Files Currently Open In Another Program")
            raise PermissionError


    @staticmethod
    def question_1n():
        """
        Question:
        Create a function that looks for through nested folders for images, and returns their metadata.
        Completed:
        03-14-2021
        """

        picture_cache = []
        def find_picmetadata(path):

            directory_ = os.listdir(path)
            for item in directory_:

                item_path = path + "\\" + item

                # If The Item Is A Folder Call Recursive Function & Look For Pictures
                if os.path.isdir(item_path):
                    find_picmetadata(item_path)

                # The Item Is A File | Append Data To Cache
                root, extension = os.path.splitext(item_path)
                if extension in [".jpeg", ".jpg", ".png", ".tiff", ".tif"]:
                    image = Image.open(item_path)
                    img_exif = image.getexif()

                    # Look For EXIF Data | Create Cleaned DF | Append To List
                    if img_exif:
                        temp_dict = {}
                        img_exif_dict = dict(img_exif)
                        for key, val in img_exif_dict.items():
                            if key in ExifTags.TAGS:
                                temp_dict[ExifTags.TAGS[key]] = val
                        temp_dict["IMAGE_NAME"] = item_path
                        picture_cache.append(temp_dict)

        # specify your path of directory
        path = r"C:\Users\renac\Documents\Programming\Python\PracticingPython\PracticeQuestions\Misc"
        find_picmetadata(path)
        print(picture_cache)
