# Name:                                            Renacin Matadeen
# Date:                                               06/08/2020
# Title                           Can Multiprocessing Improve Efficiency Accross Platforms?
#
# ----------------------------------------------------------------------------------------------------------------------
import os
import math
import multiprocessing
from Functions_Dir.cln_func import *
# ----------------------------------------------------------------------------------------------------------------------


# SECONDARY FUNCTION | Split List Evenly Per CPU Cores | Return A List Of Lists
def lists_per_core(mainlist):

    # Seperate List By Number Of CPU Cores
    chunk_size = math.ceil( len(mainlist) / os.cpu_count() )
    listofdatachunks = (mainlist[i:i + chunk_size] for i in range(0, len(mainlist), chunk_size))
    return list(listofdatachunks)


# SECONDARY FUNCTION | Run The Program With The List Of Lists & Each CPU (Worker)
def mp_compute(mainlist, str_full_list, str_abbrv_list):

    # Grab Lists For Workers
    sep_lst_for_workers = lists_per_core(mainlist)

    # Manager Will Help Store Data Created By Workers
    manager = multiprocessing.Manager()
    return_data = manager.dict()

    # Store The Processes In A List | Easier To Iterate
    processes = []

    # Register Processes | Match Number Of CPU Cores
    for i, chunk_index in enumerate(sep_lst_for_workers):
        processes.append(multiprocessing.Process(target=main_function,
                                                 args=(chunk_index, str_full_list, str_abbrv_list, i, return_data,)))

    # Start Processes
    for process in processes:
        process.start()

    # # Make Sure Processes Completes Before Moving On
    # for process in processes:
    #     process.join()

    return 1





# ----------------------------------------------------------------------------------------------------------------------
