# Name:                                            Renacin Matadeen
# Date:                                               07/01/2020
# Title                                 Data Structures: Singly Linked Lists
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from sys import getsizeof
# ----------------------------------------------------------------------------------------------------------------------

class SinglyLinkedList():
    """ Instantiate A Singly Linked List With A Sentinel Node"""

    class Node:
        """ Nodes Store Data, As Well As Pointer To Next Node Defaults to None for data, and pointer """
        __slots__ = ["data", "next"]

        def __init__(self, input_data = None, pointer = None):
            self.data = input_data
            self.next = pointer


    def __init__(self):
        """ The Linked List Will Instatiate And Set Its Head None - No Nodes """
        self.head = Node()
        self.ll_lenght = 0





# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    countries = ["Morrocco", "Canada", "Mexico", "USA", "Italy", "Germany", "France", "Canada", "United Kingdom"]

    ll = SinglyLinkedList()

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
