# Name:                                            Renacin Matadeen
# Date:                                               06/28/2021
# Title                              Main Functions That Will Query Images Provided
#
# ----------------------------------------------------------------------------------------------------------------------
import os, sys, time, re
from PIL import Image, ExifTags
# ----------------------------------------------------------------------------------------------------------------------


""" This class will take a path to a set of images, and perform a number of functions on those images  """
class ImageSet:

    


    """ On Instantiation A Dictionary Is Created To Store Paths & Date Information """
    def __init__(self):

        # Create Dictionary To Store Data
        self.nt_dict = {"FilePath": [], "DateTaken": []}


    """ This Function Will Add Image Location & Date Taken Data To Main Dictionary """
    def ingest_images(self, Folder_Path):
        image_path = Folder_Path
        
        # Iterate Through Each File In Folder
        focus_folder = os.listdir(image_path)
        for file in focus_folder:
            file_path = image_path + "/" + file

            # Filter By Image Extension
            root, extension = os.path.splitext(file_path)
            if extension in [".jpeg", ".jpg", ".png", ".tiff", ".tif"]:
                image = Image.open(file_path)
                img_exif = image.getexif()

                # Look For EXIF Data | Create Cleaned Dict | Append To Main Dict
                if img_exif:
                    temp_dict = {}
                    img_exif_dict = dict(img_exif)
                    for key, val in img_exif_dict.items():
                        if key in ExifTags.TAGS:
                            temp_dict[ExifTags.TAGS[key]] = val

            self.nt_dict["FilePath"].append(file_path)
            self.nt_dict["DateTaken"].append(temp_dict["DateTime"].replace(" ", "_"))

        print(self.nt_dict)


    """ Having Parsed Date Taken Information Change Name Of Pictures """
    def Name2DateTaken():
        pass


    """ Having Parsed Date Taken Information Ckeck If Duplicate Images Are Present """
    def IdentifyDuplicateImages():
        pass


    """ Having Identified Duplicate Images Delete Them """
    def RemoveDuplicateImages():
        pass
