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

    def lenght(self):
        """ Returns The Lenght Of The Doubly Linked List Empty | Takes O(1)"""
        return self.lenght

    def insert_top(self, input_data):
        if self.head is None:
            node = self.Node(input_data, self.head, self.tail)
            self.head = node
            self.tail = node
            self.ll_lenght += 1

    def insert_bottom(self, input_data):
        pass



# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    countries = ["Morrocco", "Canada", "Mexico", "USA", "Italy", "Germany", "France", "Canada", "United Kingdom"]

    ll = DoublyLinkedList()



# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
