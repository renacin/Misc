# Name:                                            Renacin Matadeen
# Date:                                               08/23/2020
# Title                                    Data Structures: GENERAL TREES
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------
"""
Following:
    https://www.youtube.com/watch?v=4r_XR9fUPhQ

Notes:
    +

"""

class TreeNode:
    """ This will be a General Tree node """

    def __init__(self, data):
        """ Basics For Each Node"""
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        """ This method will add a Node, as a child to your current Node """
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)

        if self.children:
            for child in self.children:
                child.print_tree()


def Build_Tree():

    # Main Node Of Tree
    root = TreeNode("Electronics")

    # Child Of Main Node
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("ThinkPad"))

    # Child Of Main Node
    cellphone = TreeNode("Cell Phones")
    cellphone.add_child(TreeNode("Iphone XR"))
    cellphone.add_child(TreeNode("Galaxy Note 10"))
    cellphone.add_child(TreeNode("One Plus 7 Pro"))

    # Child Of Main Node
    tv = TreeNode("Television")
    tv.add_child(TreeNode("Sony XBR"))
    tv.add_child(TreeNode("LG UD"))
    tv.add_child(TreeNode("Samsung DXR"))

    # Add To Main Root Node
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # Initial Setup
    root_node = Build_Tree()
    root_node.print_tree()


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
