#! /usr/bin/python

import sys
sys.path.append('../linked_list')
from list_util import Node

class Queue():
    def __init__(self, name="MyStack"):
        self.name = name
        self.head = None
        self.tail = None

    def q_print(self):
        node = self.head
        while node != None:
            print str(node.data) + " ->",
            node = node.next

        print " None"

    def enq(self, data):
        new_node = Node(data=data)
        if self.head == None:
            self.head = new_node

        if self.tail == None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def deq(self):
        if self.head == None:
            return None

        delete_node = self.head
        data = delete_node.data
        self.head = self.head.next
        delete_node = None
        return data


def test_q():
    print "##### Queue test #####"
    q = Queue()
    print "Adding to queue"
    for i in xrange(1,11,1):
        print str(i),
        q.enq(i)
    print ""
    print "Print Queue"
    q.q_print()
    print "Deleting from queue"
    for i in xrange(1, 5, 1):
        data = q.deq()
        print str(data),

    print ""
    print "Print Queue"
    q.q_print()


def main(argv):
    test_q()

if __name__ == '__main__':
    main(sys.argv)
