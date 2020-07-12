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
        self.head = None
        self.tail = None
        self._lenght = 0


    def get_lenght(self):
        """ Return The Lenght Of The Linked List | Takes O(1)"""
        return self._lenght


    def insert_top(self, input_data):
        """ Insert An Element At The Top, Right After The Head Node | Takes O(1) | Next --> """
        if (self.head is None) and (self.tail is None):
            new_node = self.Node(input_data, self.tail)
            self.head = new_node
            self._lenght += 1
            return

        elif (self.head is not None) and (self.tail is None):
            self.tail = self.head
            new_node = self.Node(input_data, self.tail)
            self.head = new_node
            self._lenght += 1
            return

        new_node = self.Node(input_data, self.head)
        self.head = new_node
        self._lenght += 1


    def display_nodes(self):
        """ Print All Elements In Linked List | Takes O(N) | Moving Left --> """
        if self.head is None:
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr = llstr + str(itr.data) + " ---> "
            itr = itr.next

        return llstr[:-6]


    def first_elem(self):
        """ Print The First Element | Takes O(1) """
        if (self.head is None):
            return

        return self.head.data


    def last_elem(self):
        """ Print The Last Element | Takes O(1) """
        if (self.tail is None):
            return

        return self.tail.data


    def reverse_list(self):
        if (self.head is None) or (self._lenght == 1):
            return

        prev = None
        itr = self.head
        while itr:
            temp = itr
            itr = itr.next
            temp.next = prev
            prev = temp

        return prev

# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    countries = ["First", "Second", "Third"]

    ll = SinglyLinkedList()
    for country in countries:
        ll.insert_top(country)

    print(ll.display_nodes())
    ll.reverse_list()

    print(ll.first_elem())
    print(ll.last_elem())
    print(ll.display_nodes())

    # print("List Lenght: {}, First Element: {}, Last Element: {}".format(
    #                                                                     ll.get_lenght(),
    #                                                                     ll.first_elem(),
    #                                                                     ll.last_elem())
    #                                                                     )

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
