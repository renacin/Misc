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


    class Node():
        """ Nodes Store Data, As Well As Pointer To Next Node Defaults to None for data, and pointer """
        __slots__ = "data", "next", "prev" # Use Slots To Improve Speed And Memory Usage


        def __init__(self, input_data = None, next_pointer = None, prev_pointer = None):
            self.data = input_data
            self.next = next_pointer
            self.prev = prev_pointer


    def __init__(self):
        """ Instantiate Head, Tail - Head Points To Tail, No Prev & Tail Points To Head, No Next """
        self.head = self.Node()
        self.tail = self.Node()
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
        """
        Insert An Element At The Top, Right After The Head Node | Takes O(1)
        Next -->
        <--- Previous
        """

        if (self.head.data is None) and (self.tail.data is None):
            new_node = self.Node(input_data, self.tail, None) # New Node On Top Equals New Head, Next Points To Tail, Prev Points To Nothing
            self.head = new_node # Head Of LL is now New Node
            self._lenght += 1 # Add To Lenght Of LinkedList


        elif (self._lenght == 1) and (self.head.data is None):
            new_node = self.Node(input_data, self.tail, None)
            self.head = new_node
            self.tail.prev = self.head
            self._lenght += 1


        elif (self._lenght == 1) and (self.head.data is not None):
            self.tail = self.head

            self.tail.next = None
            new_node = self.Node(input_data, self.tail, None)
            self.head = new_node
            self.tail.prev = self.head

            self._lenght += 1

        else:
            new_node = self.Node(input_data, self.head, None)
            self.head.prev = new_node
            self.head = new_node
            self._lenght += 1


    def insert_at_bottom(self, input_data):
        """
        Insert An Element At The Bottom, Right After The Tail Node | Takes O(1)
        Next -->
        <--- Previous
        """

        if (self.tail.data is None) and (self.head.data is None):
            new_node = self.Node(input_data, None, self.head)
            self.tail = new_node
            self._lenght += 1

        elif (self._lenght == 1) and (self.tail.data is None):
            new_node = self.Node(input_data, None, self.head)
            self.tail = new_node
            self.head.next = self.tail
            self._lenght += 1


        elif (self._lenght == 1) and (self.tail.data is not None):
            self.head = self.tail
            self.head.prev = None
            new_node = self.Node(input_data, None, self.head)
            self.head.next = new_node
            self.tail = new_node
            self._lenght += 1

        else:
            new_node = self.Node(input_data, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
            self._lenght += 1


    def top_to_bottom(self):
        """ Print The Contents Of The Linked List, Iterate Through Every Node Top To Bottom| Takes O(N)"""
        if self.head.data is None:
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr = llstr + str(itr.data) + " <---> "
            itr = itr.next

        return llstr[:-7]


    def bottom_to_top(self):
        """ Print The Contents Of The Linked List, Iterate Through Every Node | Takes O(N)"""
        if self.tail.data is None:
            return

        itr = self.tail
        llstr = ""

        while itr:
            llstr = llstr + str(itr.data) + " <---> "
            itr = itr.prev

        return llstr[:-7]


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    countries = ["Morrocco", "Canada", "America", "Italy"]
    ll = DoublyLinkedList()

    for country in countries:
        ll.insert_at_bottom(country)
        ll.insert_at_top(country)



    print(ll.get_lenght())
    print(ll.top_to_bottom())
    print(ll.bottom_to_top())


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
