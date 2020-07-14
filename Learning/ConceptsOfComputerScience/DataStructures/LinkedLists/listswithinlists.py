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



    def flattenlist(self, head):
        """ Flatten The Entire Linked List | Takes O(N)"""
        if (self.head is None):
            return

        # Find tail node of first level linked list
        temp = head
        while (temp.next != None):
            temp = temp.next
        currNode = head

        # One by one traverse through all nodes
        # of first level linked list
        # till we reach the tail node
        while(currNode != temp):

            # If current node has a child
            if(currNode.child):

                # then append the child
                # at the end of current list
                temp.next = currNode.child

                # and update the tail to new last node
                tmp = currNode.child
                while(tmp.next):
                    tmp = tmp.next
                temp = tmp

            # Change current node
            currNode = currNode.next




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

    head_node.child = Node("Node 1, Child 1, First Element")

    print("Linked List Lenght: {}".format(ll.get_lenght()))
    print("Entire Linked List: {}".format(ll.draw()))

    ll.flattenlist(head_node)
    print("Entire Linked List: {}".format(ll.draw()))


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
