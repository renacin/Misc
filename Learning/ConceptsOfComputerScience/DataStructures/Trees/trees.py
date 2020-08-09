# Name:                                            Renacin Matadeen
# Date:                                               08/07/2020
# Title                                    Data Structures: Trees In Python
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------


# This is the main tree class, will store everything
class BinaryTree:
    """ The Tree class will store everything """
    __slots__ = ["root"]

    class Node:
        """ Nodes will store data for each element as well as a pointer to the next node, or element"""
        __slots__ = ["data", "left", "right"]

        def __init__(self, input_data = None, left_pointer = None, right_pointer = None):
            self.data = input_data
            self.left = left_pointer
            self.right = right_pointer


        def insert(self, data):
            """ This method will be attached to the node class """

            # If The Root Node Is Filled
            if self.data:

                # If The Value To Be Appended Is Smaller
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)


                # If The Value To Be Appended Is Larger
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)

            # If there is no value in the root node
            else:
                self.data = data


    def __init__(self):
        """ Setup The Root Node """
        self.root = None


    def insert_data(self, input_data):
        """ Insert Function For External Method """

        # If The Root Node Is Filled
        if self.root:
            self.root.insert(input_data)

        # If there is no value in the main node
        else:
            self.root = self.Node(input_data)




# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # Create A Tree Representation
    tree = BinaryTree()

    # Inset Values
    values_to_add = [23, 24, 54, 66, 1, 34, 50, 10]
    for value in values_to_add:
        tree.insert_data(value)


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
