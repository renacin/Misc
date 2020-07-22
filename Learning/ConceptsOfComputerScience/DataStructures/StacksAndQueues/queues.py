# Name:                                            Renacin Matadeen
# Date:                                               07/19/2020
# Title                                    Data Structures: Queues In Python
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from sys import getsizeof
# ----------------------------------------------------------------------------------------------------------------------


# Remember LIFO Sequence!
class Queue():
    """ Class will store elements as a Queue. Data structure will resemble a doubly linked list"""

    class Node():
        """ Nodes will store data for each element as well as a pointer to the next node, or element"""
        __slots__ = ["data", "next"]

        def __init__(self, input_data = None, next_pointer = None, prev_pointer = None):
            self.data = input_data
            self.next = next_pointer
            self.prev = prev_pointer

    def __init__(self):
        """ Instantiate Lenght, Head, Tail For New Queue """
        self.head = None
        self.tail = None
        self._lenght = 0


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    pass

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
