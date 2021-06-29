# Name:                                            Renacin Matadeen
# Date:                                               06/28/2021
# Title                              Main Functions That Will Query Images Provided
#
# ----------------------------------------------------------------------------------------------------------------------
import os, sys, time, glob, shutil
from PIL import Image, ExifTags
# ----------------------------------------------------------------------------------------------------------------------


""" This class will take a path to a set of images, and perform a number of functions on those images  """
class ImageSet:


    """ On Instantiation A Dictionary Is Created To Store Paths & Date Information """
    def __init__(self):

        # Create Dictionaries To Store Pertinent Data
        self.img_dict = {"DateTaken": [], "FilePath": []}
        self.err_img_dict = {"FilePath": []}
        self.non_img_dict = {"FilePath": []}
        self.file_ext_dict = {"FileExtensions":[]}


    """ This Function Will Add Image Location & Date Taken Data To Main Dictionary """
    def ingest_images(self, Folder_Path):
        image_path = Folder_Path
        
        # Iterate Through Each File In Folder
        focus_folder = os.listdir(image_path)
        for file in focus_folder:
            file_path = image_path + "/" + file

            # Filter By Image Extension
            root, extension = os.path.splitext(file_path)
            if extension in [".jpeg", ".jpg", ".tiff", ".tif"]:
                image = Image.open(file_path)
                img_exif = image.getexif()

                # Look For EXIF Data | Create Cleaned Dict | Append To Main Dict
                if img_exif:
                    img_exif_dict = dict(img_exif)

                    try:
                        self.img_dict["FilePath"].append(file_path)
                        self.img_dict["DateTaken"].append(img_exif_dict[306].replace(" ", "_"))
                    
                    except KeyError:
                        print(f"Error With File: {file_path}")
                        print(img_exif_dict)
                        self.err_img_dict["FilePath"].append(file_path)

            else:
                self.non_img_dict["FilePath"].append(file_path)


            # To Better Understand Files, Collect Data On Extension Types
            if extension not in self.file_ext_dict["FileExtensions"]:
                self.file_ext_dict["FileExtensions"].append(extension)



    """ Having Parsed Date Taken Information Ckeck If Duplicate Images Are Present """
    def IdentifyDuplicateImages():
        pass


    """ Having Identified Duplicate Images Delete Them """
    def RemoveDuplicateImages():
        pass
