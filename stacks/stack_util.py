#! /usr/bin/python

from list_util import Node

class Stack():
    def __init__(self, name="MyStack"):
        self.name = name
        self.max = 0
        self.head = None

    def print_stack(self):
        node = self.head
        while node != None:
            print str(node.data) + " ->",
            node = node.next

        print " None"
        print "Max: %d" % (self.max)

    def push(self, data):
        new_node = Node(data)
        self.max = max(self.max, data)
        new_node.next = self.head
        self.head = new_node

    def peek(self):
        if self.head == None:
            return None
        return self.head.data

    def pop(self):
        if self.head == None:
            return None

        delete_node = self.head
        self.head = self.head.next
        return delete_node.data
    
