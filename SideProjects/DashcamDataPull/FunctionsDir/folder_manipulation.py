# Name:                                            Renacin Matadeen
# Date:                                               05/01/2020
# Title                                            Open CV Research
#
# ----------------------------------------------------------------------------------------------------------------------
try:
    import os
    import shutil
except ImportError:
    pass
# ----------------------------------------------------------------------------------------------------------------------


# Secondary Function Create Temp Folder That Will Store Processed Images
def create_folder(in_video_path):

    # Separate By Dash Lines | Find Folder Path
    in_path_segments = in_video_path.split("/")
    file_name = in_path_segments[-1]
    folder_path = in_video_path[:-(len(in_path_segments[-1]))]

    # Make New Folder To Store Data | TEMP
    newfolder_path = folder_path + "_TEMP_FLDR_DNT_RMV_"

    try:
        os.mkdir(newfolder_path)

    except FileExistsError:
        pass

    print("Step #1: Folder Created - 📁")

    return newfolder_path, file_name


# Secondary Function Create Temp Folder That Will Store Processed Images
def delete_folder(new_temp_folder):

    # Separate By Dash Lines | Find Folder Path
    try:
        shutil.rmtree(new_temp_folder, ignore_errors=True)
        print("Step #6: Folder Deleted - ❌")

    except:
        print("File Not Deleted")
