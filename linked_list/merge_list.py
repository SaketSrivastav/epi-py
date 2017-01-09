#!/usr/bin/python

import sys
import list_util

def merge_sorted_list(list1, list2):
    if list1.is_empty():
        list2.print_list()
        return

    if list2.is_empty():
        list1.print_list()
        return

    node1 = list1.head
    node2 = list2.head
    dummy_head = list_util.Node()
    tail = dummy_head
    while (node1 != None) and \
          (node2 != None):
        if node1.data <= node2.data:
            tail.next = node1
            tail = node1
            node1 = node1.next
        else:
            tail.next = node2
            tail = node2
            node2 = node2.next

    if node1 != None:
        tail.next = node1
    else:
        tail.next = node2

    return dummy_head.next

def test_2():
    print "###### test_2 starts ######"
    list1 = list_util.LList()
    for i in xrange(1, 7, 2):
        list1.append(i)
    list2 = list_util.LList()
    for i in xrange(2, 5, 2):
        list2.append(i)
    print "Input: "
    list1.print_list()
    list2.print_list()
    result = merge_sorted_list(list1, list2)
    print "Output: "
    list_result = list_util.LList(result)
    list_result.print_list()
    print "###### test_2 ends ######"

def test_1():
    print "###### test_1 starts ######"
    list1 = list_util.LList()
    for i in xrange(1, 7, 2):
        list1.append(i)
    list2 = list_util.LList()
    for i in xrange(2, 8, 2):
        list2.append(i)
    print "Input: "
    list1.print_list()
    list2.print_list()
    result = merge_sorted_list(list1, list2)
    print "Output: "
    list_result = list_util.LList(result)
    list_result.print_list()
    print "###### test_1 ends ######"

def test_merge_sorted_list():
    test_1()
    test_2()

def main(argv):
    test_merge_sorted_list()

if __name__ == "__main__":
    main(sys.argv)
