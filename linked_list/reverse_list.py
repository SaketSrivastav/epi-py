#! /usr/bin/python

import sys
import list_util

def reverse_list_recursive(head):
    if head == None or head.next == None:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverse_list_iterative(orig_list):
    prev_node = None
    next_node = None
    curr_node = orig_list.head
    while curr_node != None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node

def test_1():
    print "####### test_1 starts ########"
    test_list = list_util.LList()
    for i in xrange(5):
        test_list.append(i)

    print "Input: "
    test_list.print_list()
    result = reverse_list_iterative(test_list)
    dummy_list = list_util.LList(result)
    print "Output: "
    dummy_list.print_list()
    print "####### test_1 ends ########"

def test_2():
    print "####### test_2 starts ########"
    test_list = list_util.LList()
    for i in xrange(5):
        test_list.append(i)

    print "Input: "
    test_list.print_list()
    result = reverse_list_recursive(test_list.head)
    dummy_list = list_util.LList(result)
    print "Output: "
    dummy_list.print_list()
    print "####### test_1 ends ########"

def test_reverse_list():
    test_1()
    test_2()

def main(argv):
    test_reverse_list()

if __name__ == '__main__':
    main(sys.argv)
