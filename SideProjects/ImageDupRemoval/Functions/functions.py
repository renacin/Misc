# Name:                                            Renacin Matadeen
# Date:                                               06/28/2021
# Title                              Main Functions That Will Query Images Provided
#
# ----------------------------------------------------------------------------------------------------------------------
import os, shutil
from PIL import Image, ExifTags
# ----------------------------------------------------------------------------------------------------------------------


class ImageSet:
    """ This class will take a path to a set of images, and perform a number of functions on those images  """


    def __init__(self):
        """ On Instantiation A Dictionary Is Created To Store Paths & Date Information """

        # Create Dictionaries To Store Pertinent Data
        self.img_dict = {}
        self.err_img_dict = {"FilePath": []}
        self.non_img_dict = {"FilePath": []}
        self.file_ext_dict = {"FileExtensions":[]}


    def ingest_images(self, Folder_Path):
        """ This Function Will Add Image Location & Date Taken Data To Main Dictionary """

        image_path = Folder_Path
        
        # Iterate Through Each File In Folder
        focus_folder = os.listdir(image_path)
        for file in focus_folder:
            file_path = image_path + "/" + file

            # Filter By Image Extension
            root, extension = os.path.splitext(file_path)
            if extension in [".jpeg", ".jpg", ".JPG", ".tiff", ".tif"]:
                image = Image.open(file_path)
                img_exif = image.getexif()

                # Look For EXIF Data | Create Cleaned Dict | Append To Main Dict
                if img_exif:
                    img_exif_dict = dict(img_exif)

                    try:
                        date_taken = img_exif_dict[306].replace(" ", "_")
                        date_taken = date_taken.replace(":", "")
                        self.img_dict[date_taken] = file_path
                    
                    except KeyError:
                        print(f"Error With File: {file_path}")
                        self.err_img_dict["FilePath"].append(file_path)

            else:
                self.non_img_dict["FilePath"].append(file_path)


            # To Better Understand Files, Collect Data On Extension Types
            if extension not in self.file_ext_dict["FileExtensions"]:
                self.file_ext_dict["FileExtensions"].append(extension)



    def rewrite_images(self, FolderPath):
        """ Having Parsed Date Taken Information Check If Duplicate Images Are Present """

        # Ensure Folder Exists | If Not Create For Images & Misc Files
        for new_folder_name in ["CleanedImages", "MiscFiles", "ErrorFiles"]:
            focus_path = f"{FolderPath}/{new_folder_name}"
            if os.path.exists(focus_path):
                os.rmdir(focus_path)    
            os.makedirs(focus_path)

        # Iterate Through Img Dict | Write Images To Folder | Change Name To Date Taken!
        for date_taken, org_file_path in self.img_dict.items():
            root, extension = os.path.splitext(org_file_path)
            new_path = f"{FolderPath}/CleanedImages/{date_taken}{extension}"
            shutil.move(org_file_path, new_path)

        # Iterate Through Non-Img Dict | Write Images To Folder
        for org_file_path in self.non_img_dict["FilePath"]:
            file_name = org_file_path.split("/")[-1]
            new_path = f"{FolderPath}/MiscFiles/{file_name}"
            shutil.move(org_file_path, new_path)

        # Iterate Through Error Dict | Write Images To Folder
        for org_file_path in self.err_img_dict["FilePath"]:
            file_name = org_file_path.split("/")[-1]
            new_path = f"{FolderPath}/ErrorFiles/{file_name}"
            shutil.move(org_file_path, new_path)



    @staticmethod
    def rename_images():
        """ Given A Folder, This Function Will Rename JPEG images In Accordance To Their DateTaken Data"""
        pass