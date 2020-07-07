# Name:                                            Renacin Matadeen
# Date:                                               07/01/2020
# Title                                 Data Structures: Arrays Vs Linked Lists
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from sys import getsizeof
# ----------------------------------------------------------------------------------------------------------------------
"""
Links Followed:
    https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/
    https://stackabuse.com/python-linked-lists/
    https://www.youtube.com/watch?v=JlMyYuY1aXU
    https://www.youtube.com/watch?v=qp8u-frRAnU

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

        - Are fundemental to the construction of other data structures

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
        - Works With Nodes, They Contain:
            + Data
            + Pointers To Other Nodes

        - When Adding To The First / Deleting The First Elem, Is Big O(1)
        - But You Must Order So Your Adding To The First Spot

        - Need a header node to start the list

"""
# ----------------------------------------------------------------------------------------------------------------------

class SinglyLinkedList():
    """ Instantiate A Singly Linked List, Nodes Are A Class Within LinkedLists Only """

    class Node:
        """ Nodes Store Data, As Well As Pointer To Next Node Defaults to None for data, and pointer """
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

    def __init__(self):
        """ The Linked List Will Instatiate And Set Its Head None - No Nodes """
        self.head = None
        self.ll_lenght = 0

    def _insert(self, data):
        """ Method To Insert Data At Begining, Add To Lenght | Takes O(1)  """
        node = self.Node(data, self.head)
        self.head = node
        self.ll_lenght += 1

    def _delete(self):
        """ Method To Delete Data At Begining, Add To Lenght | Takes O(1)  """
        if self.head is None:
            return

        else:
            self.head = self.head.next
            self.ll_lenght -= 1

    def _lenght(self):
        """ Return The Lenght Of The Linked List, Updated Everytime A Node Is Added | Takes O(1)"""
        return self.ll_lenght

    def _printlinkedlist(self):
        """ Print The Contents Of The Linked List, Iterate Through Every Node | Takes O(N)"""
        if self.head is None:
            return "[]"

        else:
            pass
            itr = self.head
            llstr = ""

            while itr:
                llstr = llstr + str(itr.data) + ", "
                itr = itr.next

            return "[{}]".format(llstr[:-2])


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():
    pass

    # # For Array Testing
    # arr_lst = array_list(10000)
    # print("Size Of Array: {} [KiloBytes]".format(getsizeof(arr_lst) / 1024))

    # For LinkedList Testing
    countries = ["Morrocco", "Canada", "Mexico", "USA", "Italy", "Germany", "France", "United Kingdom"]

    ll = SinglyLinkedList()
    for country in countries:
        ll._insert(country)

    ll._delete()

    print(ll._printlinkedlist())
    print(ll._lenght())



# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
