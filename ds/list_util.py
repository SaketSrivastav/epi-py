#! /usr/bin/python

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


class LList():
    def __init__(self, node=None, name="List"):
        self.head = node
        self.name = name

    def print_list(self):
        print self.name + ": ",
        temp = self.head
        while temp != None:
            print "%s -> " % (str(temp.data)),
            temp = temp.next
        print "None"

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node

    def delete(self, pos=0):
        if self.head == None:
            return None
        if pos > self.count():
            return None

        temp = self.head
        prev = None
        while temp != None and index != pos:
            prev = temp
            temp = temp.next

        if temp == None:
            return None

        delete_data = temp.data
        prev.next = temp.next
        return delte_data

    def get_node(self, pos=0):
        if pos < 0:
            return -1

        temp = self.head
        while temp != None and pos >= 0:
            if pos == 0:
                return temp
            temp = temp.next
            pos -= 1

    def count(self):
        cnt = 0
        temp = self.head
        while temp != None:
            cnt += 1
            temp = temp.next
        return cnt

    def is_empty(self):
        if self.head == None:
            return True
        return False
