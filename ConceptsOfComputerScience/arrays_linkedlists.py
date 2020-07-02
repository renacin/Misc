# Name:                                            Renacin Matadeen
# Date:                                               07/01/2020
# Title                                 Data Structures: Arrays Vs Linked Lists
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------
"""
Notes:
    + What Is The Difference Between Linked Lists And Arrays

    + Arrays
        - One of the simplist data structures in programming
        - Arrays are index based structures, where each element has an associated index
        - Arrays are stored in sequential blocks of memory
        - Size of arrays are specified during allocations

    + Linked Lists
        - A linked list is a linear data structure
        - Is not index based, but rather based on nodes with references
        - A node contains the data, as well as pointers to the next data source, or even the previous
        - Data are not stored in contiguous memory locations; rather randomly stored

    + Linked Lists Prefered When:
        - Constant-time insertions/deletions from the list, dependence on time is critical
        - Have no clue how many items will be in the list
        - Don't need random access to any elements

    + Arrays Peferable When:

        - Need indexed/random access to elements
        - Know the number of elements in the array ahead of time
        - Speed when iterating through all the elements in sequence
        - Memory is a concern



Jot Notes:
    Time To Append 1 Data Point To End
        - Array Elem 1_000_000         Time = 0.010011434555053711    [1x]
        - Array Elem 2_000_000         Time = 0.021019935607910156    [2x]
        - Array Elem 5_000_000         Time = 0.049993276596069336    [5x]

"""
# ----------------------------------------------------------------------------------------------------------------------


def array_list(n):
    list_array = [x for x in range(n)]
    return list_array


def main():
    arr_lst = array_list(5_000_000)
    start = time.time()
    arr_lst = arr_lst.append(1)
    end = time.time()
    print("Time Elapsed: {}".format(end - start))

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
