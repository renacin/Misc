# Name:                                            Renacin Matadeen
# Date:                                               07/19/2020
# Title                                    Data Structures: Queues In Python
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from sys import getsizeof
# ----------------------------------------------------------------------------------------------------------------------


# Remember LIFO Sequence!
class Queue():
    """ Class will store elements as a Queue. Data structure will resemble a doubly linked list"""

    class Node():
        """ Nodes will store data for each element as well as a pointer to the next node, or element"""
        __slots__ = ["data", "next", "prev"]

        def __init__(self, input_data = None, next_pointer = None, prev_pointer = None):
            self.data = input_data
            self.next = next_pointer
            self.prev = prev_pointer


    def __init__(self):
        """ Instantiate Lenght, Head, Tail For New Queue """
        self.head = None
        self.tail = None
        self._lenght = 0

    def empty_queue(self):
        """ Returns True/False Is The Queue Empty | Takes O(1)"""
        return self._lenght == 0

    def queue_len(self):
        """ Returns Lenght Of Queue | Takes O(1)"""
        return self._lenght

    def enqueue(self, input_data):
        """ Add Data To The Queue, Be Mindful Of FIFO Structure """

        # If Queue Is Empty
        if self._lenght == 0:
            new_node = self.Node(input_data)
            self.head = new_node
            self.tail = self.head
            self._lenght += 1
            return

        # If Queue Only Has One Value
        elif self._lenght == 1:
            new_node = self.Node(input_data)
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
            self._lenght += 1
            return

        # If Queue Has Two Values In It
        new_node = self.Node(input_data)
        new_node.next = self.tail
        self.tail.prev = new_node
        self.tail = new_node
        self._lenght += 1

    def dequeue(self):
        """ Remove Data From The Top Of The Queue, Be Mindful Of FIFO Structure """
        if self._lenght == 0:
            return

        before_head = self.head.prev
        self.head = before_head
        self.head.next = None
        self._lenght -= 1

    def print_queue(self):
        """ Start From Head And Work Your Way Down | Takes O(N)"""
        if self._lenght == 0:
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr = llstr + " --- " + str(itr.data)
            itr = itr.prev

        return llstr[5:]

# ----------------------------------------------------------------------------------------------------------------------


# MAIN FUNCTION WILL STORE TESTING
def main():

    # Create A Queue
    main_queue = Queue()

    # You Own A Restaurant, Here Are Your Orders
    orders = ["Lisa: Soup", "Gary: Fries", "Dave: Burger", "Mary: Pizza"]

    for order in orders:
        main_queue.enqueue(order)

    print(main_queue.print_queue())

    # You Finish The First Order
    main_queue.dequeue()
    print(main_queue.print_queue())

    # You Finish The Second Order
    main_queue.dequeue()
    print(main_queue.print_queue())

    # Another Customer Places An Order
    main_queue.enqueue("David: Salad")
    print(main_queue.print_queue())

    # You Finish The Third Order
    main_queue.dequeue()
    print(main_queue.print_queue())



# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
