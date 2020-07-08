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
        def __init__(self, data = None, next_pointer = None, prev_pointer = None):
            self.data = data
            self.next = next_pointer
            self.prev = prev_pointer


    def __init__(self):
        """ The Doubly Linked List Will Instatiate And Set Its Head To None - No Nodes """
        self.head = None
        self.tail = None
        self.ll_lenght = 0

    def insert(self, input_data):
        if self.head is None:
            node = self.Node(input_data, self.head, self.tail)
            self.head = node
            self.tail = node
            self.ll_lenght += 1



# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    countries = ["Morrocco", "Canada", "Mexico", "USA", "Italy", "Germany", "France", "Canada", "United Kingdom"]

    ll = DoublyLinkedList()
    ll.insert("Canada")


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
