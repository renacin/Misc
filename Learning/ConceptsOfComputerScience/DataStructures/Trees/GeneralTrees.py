# Name:                                            Renacin Matadeen
# Date:                                               08/07/2020
# Title                                    Data Structures: BINARY SEARCH TREES
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------


class Node:
    """ This will be a tree node """

    def __init__(self, data):
        """ Basics For Each Node"""
        self.data = data
        self.children = []

    def insert(self, data):
        """ This method will be attached to a node """
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # Initial Setup
    pass


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
