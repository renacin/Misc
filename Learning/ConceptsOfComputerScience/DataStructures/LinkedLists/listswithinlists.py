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

    + Move Node class outside. Doesn't make things too complicated, and gives you the option to add nodes after the fact
        and without the need of a function within the linked list class

"""
# ----------------------------------------------------------------------------------------------------------------------


class Node():
    """ Nodes Store Data, As Well As Pointer To Next Node Defaults to None for data, and pointer """
    __slots__ = ["data", "next", "child"]

    def __init__(self, input_data = None, pointer = None):
        self.data = input_data
        self.next = pointer
        self.child = None


class SinglyLinkedList():
    """ Instantiate A Singly Linked List With A Sentinel Node"""

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
            new_node = Node(input_data)
            self.head = new_node
            self._lenght += 1
            return

        elif (self.head is not None) and (self.tail is None):
            new_node = Node(input_data, self.head)
            self.tail = self.head
            self.head = new_node
            self._lenght += 1
            return

        new_node = Node(input_data, self.head)
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


    def return_top_node(self):
        """ Returns Top Node So User Can Add Nodes As Desired | Takes O(1)"""
        if (self.head is None):
            return

        return self.head


    def has_child(self, _depth, cur_node, counter):

        itr = cur_node
        while itr:
            if (itr.child is not None):
                print("Child Found At: Depth {}, Element {}".format(_depth, counter))
                self.has_child(_depth + 1, itr.child, counter)
                itr.next
                counter += 1

            elif (itr.child is None) and (itr.next is None):
                return

            else:
                itr = itr.next
                counter += 1


    def check_for_child(self):
        """ Loop Through Entire Linked List And Find All Child Nodes | Takes O(N)"""
        # Should I Use Recursion To Make Things Easier?
        if (self.head is None):
            return

        itr = self.head

        while itr:
            self.has_child(1, itr, 0)


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # Create Main Linked List, Contains Inner Linkeed List
    ll_items = ["First Element", "Second Element", "Third Element"]
    ll = SinglyLinkedList()
    for item in ll_items:
        ll.insert_top(item)

    # Add Child Linked List To Top Node
    head_node = ll.return_top_node()

    head_node.next.child = Node("Node 2, Child 1, First Element")
    head_node.next.child.next = Node("Node 2, Child 1, Second Element")



    print("Linked List Lenght: {}".format(ll.get_lenght()))
    print("Entire Linked List: {}".format(ll.draw()))
    ll.check_for_child()


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()