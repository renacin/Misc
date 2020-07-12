# Name:                                            Renacin Matadeen
# Date:                                               07/01/2020
# Title                                 Data Structures: Singly Linked Lists
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from sys import getsizeof
# ----------------------------------------------------------------------------------------------------------------------

class SinglyLinkedList():
    """ Instantiate A Singly Linked List With A Sentinel Node"""

    class Node:
        """ Nodes Store Data, As Well As Pointer To Next Node Defaults to None for data, and pointer """
        __slots__ = ["data", "next"]

        def __init__(self, input_data = None, pointer = None):
            self.data = input_data
            self.next = pointer


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
        if (self.head is None):                                               # If List Is Empty
            new_node = self.Node(input_data)
            self.head = new_node
            self._lenght += 1
            return

        elif (self.head is not None) and (self.tail is None):                 # If Head Is Full, But Tail Empty
            new_node = self.Node(input_data, self.head)
            self.tail = self.head
            self.head = new_node
            self._lenght += 1
            return

        new_node = self.Node(input_data, self.head)
        self.head = new_node
        self._lenght += 1


    def reverse(self):
        """
        Reverse The Linked List | Takes O(N)
        Iterate through your original linked list. While doing so create a new linked list where the pointers point
        to in the opposite direction. Once finished, the head of your original list is now the head of your reversed
        list.
        """
        counter = 0
        prev = None                             # Set previous node to node
        itr = self.head                         # Set your iterable, start at the top of your linked list

        while itr:                              # While self.head does not equal to None

            if (counter == 0):
                self.tail = itr
                counter += 1

            temp = itr                          # Temp variable is equal to the node that your at
            itr = itr.next                      # itr is now the next node
            temp.next = prev                    # Your temp node (current node) now points to the previous
            prev = temp                         # Your previous now equals the current node

        self.head = prev                        # Set the new head of you linked list as prev. Contains new pointers


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

    def top_element(self):
        """ Return The Element Currently On Top Of The LL | Takes O(1)"""
        if (self.head is None):
            return

        return self.head.data

    def last_element(self):
        """ Return The Element Currently On Top Of The LL | Takes O(1)"""
        if (self.tail is None):
            return

        return self.tail.data

# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    countries = ["First", "Second", "Third"]

    ll = SinglyLinkedList()
    for country in countries:
        ll.insert_top(country)

    print("Linked List Lenght: {}".format(ll.get_lenght()))

    ll.reverse()
    print("Top Element: {}".format(ll.top_element()))
    print("Entire Linked List: {}".format(ll.draw()))
    print("Last Element: {}".format(ll.last_element()))

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
