# Name:                                            Renacin Matadeen
# Date:                                               07/01/2020
# Title                                  Data Structures: Circular Linked Lists
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------


class CircularLinkedList():
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
        self._lenght = 0


    def get_lenght(self):
        """ Return The Lenght Of The Linked List | Takes O(1)"""
        return self._lenght


    def insert_top(self, input_data):
        """ Insert An Element At The Top, Right After The Head Node | Takes O(1) | Next --> """
        # Empty List, Default Layout
        if (self.head is None) and (self._lenght == 0):
            new_node = self.Node(input_data)
            self.head = new_node
            self.head.next = self.head
            self._lenght += 1
            return

        elif (self.head is not None) and (self._lenght == 1):
            self.tail = self.head
            new_node = self.Node(input_data, self.tail)
            self.head = new_node
            self.tail.next = self.head
            self._lenght += 1
            return

        new_node = self.Node(input_data, self.head)
        self.head = new_node
        self.tail.next = self.head
        self._lenght += 1


    def loop_nodes(self):
        """ Print All Elements In Linked List | Takes O(N) | Moving Left --> | Be Careful Of Infinite Loop!"""
        if self.head is None:
            return

        counter = 1
        itr = self.head
        llstr = ""

        while (counter <= self._lenght):
            llstr = llstr + str(itr.data) + " ---> "
            itr = itr.next
            counter += 1

        return llstr[:-6]


    def iterate_nodes(self, num_of_terations):
        if self.head is None:
            return

        else:
            itr = self.head
            for number in range(num_of_terations):
                print(str(itr.data))
                itr = itr.next

            return


# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # For LinkedList Testing
    countries = ["America", "Canada", "Mexico"]

    ll = CircularLinkedList()
    for country in countries:
        ll.insert_top(country)

    print("Lenght: {}".format(ll.get_lenght()))
    ll.iterate_nodes(6)


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
