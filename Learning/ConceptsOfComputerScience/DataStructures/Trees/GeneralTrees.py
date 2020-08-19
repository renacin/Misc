# Name:                                            Renacin Matadeen
# Date:                                               08/07/2020
# Title                                    Data Structures: BINARY SEARCH TREES
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------


class Node:
    """ This will be a General Tree node """

    def __init__(self, data):
        """ Basics For Each Node"""
        self.parent = None
        self.children = []
        self.data = data


    def add_child(self, child):
        """ This method will add a Node, as a child to your current Node """
        child.parent = self
        self.children.append(child)



# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # Initial Setup
    pass


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
