# Name:                                            Renacin Matadeen
# Date:                                               08/07/2020
# Title                                    Data Structures: Trees In Python
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------


# Remember Hierarchy!
class Node:
    """ This will be a tree node """


    def __init__(self, data):
        """ Basics For Each Node"""
        self.left = None
        self.right = None
        self.data = data


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


    def PrintTree(self):
        """ This method will be attached to the main node, and print each associated value """
        if self.left:
            self.left.PrintTree()

        print(self.data)

        if self.right:
            self.right.PrintTree()

# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # Create A Root Node
    root_node = Node(12)

    # Inset Values
    values_to_add = [23, 54, 77, 1, 2, 4, 5]
    for value in values_to_add:
        root_node.insert(value)

    # Print Tree
    root_node.PrintTree()


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
