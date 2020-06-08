# Name:                                            Renacin Matadeen
# Date:                                               05/28/2020
# Title                           Precursor To Street Cleaning Program - Understand The Data
#
# ----------------------------------------------------------------------------------------------------------------------
from Functions_Dir.mp_func import *
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION | Stores General Flow Of Program
def main():

    # Read Street Abbrv To Be Passed Into Function: expand_str
    str_abbrv = pd.read_csv(r"C:\Users\renac\Documents\Programming\Python\Misc\StreetName_CleanUp\Data\StreetAbbrv.csv")
    str_full_list = list(str_abbrv["Full"])
    str_abbrv_list = list(str_abbrv["Abbrv"])

    # Import The CSV File | Drop Duplicates
    street_name_col = "LF_NAME"
    raw_data = pd.read_csv(r"C:\Users\renac\Desktop\Misc\CityCentreLine\Data.csv")

    # Create A Multiprocessing Function That Takes The
    data = mp_compute(raw_data[street_name_col], str_full_list, str_abbrv_list)







    # # New Column Equal List Comprehension Creation
    # raw_data["Cleaned_ADDR"] = [main_clean(x, str_full_list, str_abbrv_list) for x in raw_data[street_name_col]]
    #
    # # Export Data
    # raw_data.to_csv(r"C:\Users\renac\Desktop\Test.csv", index=False)


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()









# def process_frames_multiprocessing(new_temp_folder, file_name):
#
#     # Create Main Data Storage Unit
#     main_data_container = {'Frame_Num': [], 'Date': [], 'Time': [],
#                            'Latitude': [], 'Longitude': [], 'Speed': []}
#
#     # Manager Will Help Store Data Created By Workers
#     manager = multiprocessing.Manager()
#     return_data = manager.dict()
#
#     # List Of Dif Indices
#     multiple_chunks_list = calc_indices_per_core(new_temp_folder)
#
#     # Store The Processes In A List | Easier To Iterate
#     processes = []
#
#     # Register Processes | Match Number Of CPU Cores
#     for i, chunk_index in enumerate(multiple_chunks_list):
#
#         # Utilize Multiprocessing To Process Frames To Data
#         processes.append(multiprocessing.Process(target=process_frames,
#                                                  args=(new_temp_folder, chunk_index, i + 1, return_data,)))
#
#     # Start Processes
#     for process in processes:
#         process.start()
#
#     # Make Sure Processes Completes Before Moving On
#     for process in processes:
#         process.join()
#
#     print("Step #4: Workers Finished Processing - ⛏️")
#
#     # Print Data Stored By Processors
#     for dataset_ in return_data.values():
#
#         # Append Data Parsed By Workers
#         main_data_container["Frame_Num"].extend(dataset_["Frame_Num"])
#         main_data_container["Date"].extend(dataset_["Date"])
#         main_data_container["Time"].extend(dataset_["Time"])
#         main_data_container["Latitude"].extend(dataset_["Latitude"])
#         main_data_container["Longitude"].extend(dataset_["Longitude"])
#         main_data_container["Speed"].extend(dataset_["Speed"])
#
#     # Create A Pandas DF | Write To Folder
#     csv_path = new_temp_folder.replace("_TEMP_FLDR_DNT_RMV_", "")
#     file_name = file_name.replace(".mp4", "")
#     new_path = csv_path + file_name + ".csv"
#
#     df = pd.DataFrame(main_data_container)
#     df.to_csv(new_path, index=False)
#     print("Step #5: Data Written - 💾")
