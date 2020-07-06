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



# Creating A Subclass Of The Linked List
class node_ll:
    # Nodes Store Data, As Well As Pointer To Next Node [Default Is None In Case It's The Last One]
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next



class SinglyLinkedList():
    # Initialize The Head Node, Will Not Contain Data, Just Initiates First Point
    def __init__(self):
        self.head = None


    # Method To Insert Data At Begining | Takes O(1)
    def insert_begin(self, data):
        node = node_ll(data, self.head)
        self.head = node


    # Method To Insert Data At The End | Takes O(N)
    def insert_end(self, data):

        # If No Data In Linked List
        if self.head is None:
            self.head = node_ll(data, None)

        # Loop Through All Nodes To The End
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node_ll(data, None)


    # Method To Print Your LinkedList | Depends On self.head
    def print_ll(self):
        if self.head is None:
            print("Linked List Is Empty")
            return

        else:
            itr = self.head
            llstr = ""

            # Pull Data In Current Itertor Node, The Move Next To Other Node, Redo While Loop
            while itr:
                llstr = llstr + str(itr.data) + ", "
                itr = itr.next

            print("Linked List: [{}]".format(llstr[:-2]))


    # Method To Print Lenght Of Linked List | Takes O(N)
    def print_len(self):
        ll_lenght = 0
        itr = self.head

        while itr:
            ll_lenght += 1
            itr = itr.next

        return ll_lenght


    # Delete First Item | Should Be O(1)
    def del_begin(self):

        # If No Data In Linked List
        if self.head is None:
            print("No Data To Delete")

        # Loop Through All Nodes To The End
        else:
            self.head = self.head.next


    # Delete Last Item | Should Be O(N)
    def del_last(self):

        # If No Data In Linked List
        if self.head is None:
            print("No Data To Delete")
            return

        else:
            # Loop Through Get Lenght
            ll_lenght = 0
            itr_1 = self.head
            itr_2 = self.head

            while itr_1:
                ll_lenght += 1
                itr_1 = itr_1.next

            itr_2 = self.head
            while ll_lenght > 2:
                ll_lenght -= 1
                print(itr_2.data)
                itr_2 = itr_2.next

            itr_2.next = None



    # Create A Deconstructor Method To Delete Everything | Needs Further Refinement
    def __del__(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():
    pass

    # # For Array Testing
    # arr_lst = array_list(10000)
    # print("Size Of Array: {} [KiloBytes]".format(getsizeof(arr_lst) / 1024))

    # For LinkedList Testing
    countries = ["Canada", "Mexico", "USA", "Italy", "Germany", "France", "United Kingdom"]

    ll = SinglyLinkedList()
    for country in countries:
        ll.insert_begin(country)
        ll.insert_end(country)

    ll.del_last()
    ll.print_ll()
    ll.print_len()

    del ll


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
