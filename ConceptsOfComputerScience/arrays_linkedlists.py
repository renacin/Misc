# Name:                                            Renacin Matadeen
# Date:                                               07/01/2020
# Title                                 Data Structures: Arrays Vs Linked Lists
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------
"""
Links Followed:
    https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/

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
    + Time To Append 1 Data Point To End
        - Array Elem 1_000_000         Time = 0.010011434555053711    [1x]
        - Array Elem 2_000_000         Time = 0.021019935607910156    [2x]
        - Array Elem 5_000_000         Time = 0.049993276596069336    [5x]

    + Linked Lists
        - Need a header node to start the list

"""
# ----------------------------------------------------------------------------------------------------------------------



# Creating A Structure For Singly Linked Lists
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class SinglyLinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node



# Utilizing A Structure For Array Lists
def array_list(n):
    list_array = [x for x in range(n)]
    return list_array




# MAIN FUNCTION WILL STORE TESTING
def main():

    # For Array Testing
    arr_lst = array_list(100)

    # For Linked List Testing
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(15)
    linked_list.traverse_list()



# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
