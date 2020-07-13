# Name:                                            Renacin Matadeen
# Date:                                               07/13/2020
# Title                           Data Structures: Singly Linked Lists Within Linked List
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from sys import getsizeof
# ----------------------------------------------------------------------------------------------------------------------
"""
Notes:
    + Multi-Level Linked Lists Are Quite Complex, But Useful Data Structures

"""
# ----------------------------------------------------------------------------------------------------------------------

class SinglyLinkedList():
    """ Instantiate A Singly Linked List With A Sentinel Node"""

    class Node():
        """ Nodes Store Data, As Well As Pointer To Next Node Defaults to None for data, and pointer """
        __slots__ = ["data", "next", "child"]

        def __init__(self, input_data = None, pointer = None):
            self.data = input_data
            self.next = pointer
            self.child = None


    def __init__(self):
        """ The Linked List Will Instatiate And Set Its Head None - No Nodes """
        self.head = None
        self.tail = None
        self._lenght = 0


    def get_lenght(self):
        """ Return The Lenght Of The Linked List | Takes O(1)"""
        return self._lenght

    def insert_top(self, input_data):
        """ Insert A New Node Of Data At The Top Of The List | Takes O(1)"""
        if (self.head is None):
            new_node = self.Node(input_data)
            self.head = new_node
            self._lenght += 1
            return

        elif (self.head is not None) and (self.tail is None):
            new_node = self.Node(input_data, self.head)
            self.tail = self.head
            self.head = new_node
            self._lenght += 1
            return

        new_node = self.Node(input_data, self.head)
        self.head = new_node
        self._lenght += 1


    def draw(self):
        """ Return The Entire Linked Lists As A String | Takes O(N)"""
        if (self.head is None):
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr = llstr + str(itr.data) + " ---> "
            itr = itr.next

        return llstr[:-6]


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # Create Main Linked List, Contains Inner Linkeed List
    ll_items = ["First", "Second", "Third", "Fourth", "Fifth"]
    ll = SinglyLinkedList()
    for item in ll_items:
        ll.insert_top(item)

    print("Linked List Lenght: {}".format(ll.get_lenght()))
    print("Entire Linked List: {}".format(ll.draw()))


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
