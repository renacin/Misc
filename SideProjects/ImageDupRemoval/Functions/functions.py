# Name:                                            Renacin Matadeen
# Date:                                               06/28/2021
# Title                              Main Functions That Will Query Images Provided
#
# ----------------------------------------------------------------------------------------------------------------------
import os, sys, time, re
# ----------------------------------------------------------------------------------------------------------------------


""" This class will take a path to a set of images, and perform a number of functions on those images  """
class ImageSet:


    """ Providing A Path, This  """
    def __init__(self, Folder_Path):

        # Injest Path
        self.image_path = Folder_Path

        # Pull Image Names Into List
        image_list = os.listdir(self.image_path)
        for x in image_list:
            print(x)
            time.sleep(1)

        number_files = len(image_list)
        print(number_files)

