# Name:                                            Renacin Matadeen
# Date:                                               07/19/2020
# Title                                    Data Structures: Stacks In Python
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from sys import getsizeof
# ----------------------------------------------------------------------------------------------------------------------


# Remember LIFO Sequence!
class Stack():
    """ Class will store elements as a Stack. Data structuree will resemble a singly linked list"""

    class Node():
        """ Nodes will store data for each element as well as a pointer to the next node, or element"""
        __slots__ = ["data", "next"]

        def __init__(self, input_data = None, pointer = None):
            self.data = input_data
            self.next = pointer

    def __init__(self):
        """ Instantiate Lenght And Head For New Stack """
        self.head = None
        self._lenght = 0

    def push(self, input_data):
        """ Add New Element To Top Of Stack """
        new_node = self.Node(input_data, self.head)
        self.head = new_node
        self._lenght += 1
        return

    def pop(self):
        """ Remove Top Element In Stack """
        if (self.head is None):
            return

        top_val = self.head
        self.head = top_val.next
        self._lenght -= 1
        return

    def top(self):
        """ Return Top Elemnt In Stack """
        if (self.head is None):
            return

        return self.head.data


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    cds = ["0001", "0002", "0003", "0004", "0005"]
    cd_stack = Stack()
    for cd in cds:
        cd_stack.push(cd)

    cd_stack.pop()
    print(cd_stack.top())

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
