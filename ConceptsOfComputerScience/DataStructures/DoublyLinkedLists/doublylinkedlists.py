# Name:                                            Renacin Matadeen
# Date:                                               07/07/2020
# Title                                 Data Structures: Doubly Linked Lists
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from sys import getsizeof
# ----------------------------------------------------------------------------------------------------------------------
"""
Links Followed:

"""
# ----------------------------------------------------------------------------------------------------------------------

class DoublyLinkedList():
    """ Instantiate A Doubly Linked List, Nodes Are A Class Within DoublyLinkedLists Only """


    class Node:
        """ Nodes Store Data, As Well As Pointer To Next Node Defaults to None for data, and pointer """
        __slots__ = "data", "next", "prev" # Use Slots To Improve Speed And Memory Usage


        def __init__(self, input_data = None, next_pointer = None, prev_pointer = None):
            self.data = input_data
            self.next = next_pointer
            self.prev = prev_pointer


    def __init__(self):
        """ Instantiate Head, Tail - Head Points To Tail, No Prev & Tail Points To Head, No Next """
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._lenght = 0


    def is_empty(self):
        """ Returns True/False Is The Doubly Linked List Empty | Takes O(1)"""
        return self._lenght == 0

    def get_lenght(self):
        """ Returns The Lenght Of The Doubly Linked List Empty | Takes O(1)"""
        return self._lenght

    def insert_at_top(self, input_data):
        """ Insert An Element At The Top, Right After The Head Node | Takes O(1)"""
        new_node = self.Node(input_data, self.tail, None)

        if self._lenght == 0:
            self.head = new_node
            self._lenght += 1


    def insert_at_bottom(self, input_data):
        pass


    def dll_nodes(self):
        """ Print The Contents Of The Linked List, Iterate Through Every Node | Takes O(N)"""
        if self._lenght == 0:
            return

        itr = self.head
        llstr = ""

        while itr:
            if itr.data is not None:
                llstr = llstr + str(itr.data) + " <---> "
            itr = itr.next

        return llstr[:-7]



# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    countries = ["Morrocco", "Canada", "Mexico", "USA", "Italy", "Germany", "France", "Canada", "United Kingdom"]

    ll = DoublyLinkedList()
    ll.insert_at_top("Canada")
    print(ll.get_lenght())
    print(ll.dll_nodes())


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
