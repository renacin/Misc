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
        def __init__(self, data = None, pointer = None):
            self.data = data
            self.next = pointer


    def __init__(self):
        """ The Linked List Will Instatiate And Set Its Head None - No Nodes """
        self.head = None
        self.ll_lenght = 0


    def _insertT(self, data):
        """ Method To Insert Data At Begining, Add To Lenght | Takes O(1)  """
        node = self.Node(data, self.head)
        self.head = node
        self.ll_lenght += 1


    def _inset_AFTR_IDX(self, target_idx, _data):
        """ Method To Insert Data After Index | Takes O(N)  """
        ll_lenght = self._lenght()

        if self.head is None:
            raise Exception("Empty Linked List")

        elif (target_idx > (ll_lenght - 1)) or (target_idx < 0):
            raise Exception("Invalid Index")

        ll_index = 0
        itr = self.head                                 # Get First Node
        while itr:                                      # Loop Through Nodes, Find Matching Index
            if target_idx == ll_index:
                node = self.Node(_data, itr.next)       # Create New Node, This Node Now Points To Other Data
                itr.next = node                         # The Index Node Now Points To The New Node

            ll_index += 1
            itr = itr.next


    def _deleteT(self):
        """ Method To Delete Data At Begining, Add To Lenght | Takes O(1)  """
        if self.head is None:
            return

        self.head = self.head.next
        self.ll_lenght -= 1


    def _lenght(self):
        """ Return The Lenght Of The Linked List, Updated Everytime A Node Is Added | Takes O(1)"""
        return self.ll_lenght


    def _printT(self):
        """ Print The Node On First In The Linked List Stack | Takes O(1)"""
        if self.head is None:
            return None

        return self.head.data


    def _printB(self):
        """ Print The Node Last In The Linked List Stack | Takes O(N)"""
        if self.head is None:
            return None

        itr = self.head
        while itr:
            itr_data = itr.data
            itr = itr.next

        return itr_data


    def _printlinkedlist(self):
        """ Print The Contents Of The Linked List, Iterate Through Every Node | Takes O(N)"""
        if self.head is None:
            return "[]"

        itr = self.head
        llstr = ""

        while itr:
            llstr = llstr + str(itr.data) + " ---> "
            itr = itr.next

        return llstr[:-6]


    def _isin(self, input_data):
        """ Check To See If Value Is In LinkedList, Iterate Through Every Node | Takes O(N)"""
        isin_statement = False

        if self.head is None:
            pass

        itr = self.head
        while itr:
            if itr.data == input_data:
                isin_statement = True
                break

            itr = itr.next

        return isin_statement


    def _getindex(self, input_data):
        """ Get Index Of Provided Data, Return List | Takes O(N)"""
        idx = []

        if self.head is None:
            return idx

        counter = 0
        itr = self.head
        while itr:
            if itr.data == input_data:
                idx.append(counter)
                itr = itr.next
                counter += 1

            itr = itr.next
            counter += 1

        return idx


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    countries = ["Morrocco", "Canada", "Mexico", "USA", "Italy", "Germany", "France", "Canada", "United Kingdom"]

    ll = SinglyLinkedList()
    for country in countries:
        ll._insertT(country)

    ll._inset_AFTR_IDX(0, "Jamaica")
    print(ll._printlinkedlist())

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
