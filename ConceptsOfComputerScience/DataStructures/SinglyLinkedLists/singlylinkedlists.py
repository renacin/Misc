# Name:                                            Renacin Matadeen
# Date:                                               07/01/2020
# Title                                 Data Structures: Singly Linked Lists
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from sys import getsizeof
# ----------------------------------------------------------------------------------------------------------------------
"""
Links Followed:
    https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/
    https://stackabuse.com/python-linked-lists/
    https://www.youtube.com/watch?v=JlMyYuY1aXU
    https://www.youtube.com/watch?v=qp8u-frRAnU
"""
# ----------------------------------------------------------------------------------------------------------------------

class SinglyLinkedList():
    """ Instantiate A Singly Linked List, Nodes Are A Class Within LinkedLists Only """


    class Node:
        """ Nodes Store Data, As Well As Pointer To Next Node Defaults to None for data, and pointer """
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next


    def __init__(self):
        """ The Linked List Will Instatiate And Set Its Head None - No Nodes """
        self.head = None
        self.ll_lenght = 0


    def _insertT(self, data):
        """ Method To Insert Data At Begining, Add To Lenght | Takes O(1)  """
        node = self.Node(data, self.head)
        self.head = node
        self.ll_lenght += 1


    def _insertB(self, data):
        """ Method To Insert Data At The End Of A Linked List, Add To Lenght | Takes O(N)  """
        node = self.Node(data, self.head)
        self.head = node
        self.ll_lenght += 1


    def _deleteT(self):
        """ Method To Delete Data At Begining, Add To Lenght | Takes O(1)  """
        if self.head is None:
            return

        else:
            self.head = self.head.next
            self.ll_lenght -= 1


    def _lenght(self):
        """ Return The Lenght Of The Linked List, Updated Everytime A Node Is Added | Takes O(1)"""
        return self.ll_lenght


    def _printlinkedlist(self):
        """ Print The Contents Of The Linked List, Iterate Through Every Node | Takes O(N)"""
        if self.head is None:
            return "[]"

        else:
            pass
            itr = self.head
            llstr = ""

            while itr:
                llstr = llstr + str(itr.data) + ", "
                itr = itr.next

            return "[{}]".format(llstr[:-2])


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():
    pass

    # For LinkedList Testing
    countries = ["Morrocco", "Canada", "Mexico", "USA", "Italy", "Germany", "France", "United Kingdom"]

    ll = SinglyLinkedList()
    for country in countries:
        ll._insertT(country)

    ll._deleteT()

    print(ll._printlinkedlist())
    print(ll._lenght())

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
