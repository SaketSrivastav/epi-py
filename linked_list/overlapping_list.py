#! /usr/bin/python
import sys
import list_util

def is_overlapping_list(head1, head2):
    """
    Input: list1 and list2
    Output: Overlapping node or None
    Description: If 2 list overlap then they will have common tail node. Let x
    be length of list1 and y be length of list2. x-y gives you the difference
    by which both list are apart. Move longer list by this difference and then
    move both list together. The point where they meet is the overlapping node.
    """
    if head1 == None:
        print "head1 is None"
        return head2

    if head2 == None:
        print "head2 is None"
        return head

    dummy_list = list_util.LList(head1)
    len_A = dummy_list.count()

    dummy_list = list_util.LList(head2)
    len_B = dummy_list.count()

    print "len_A: %d len_B: %d" % (len_A, len_B)
    if len_A >= len_B:
        long_list = head1
        short_list = head2
    else:
        long_list = head2
        short_list = head1
    print "long_list: %d short_list: %d" % (long_list.data, short_list.data)
    diff_len = abs(len_A - len_B)
    while diff_len > 0:
        long_list = long_list.next
        diff_len -= 1

    print "long_list moved to %d" % (long_list.data)
    while long_list != None and short_list != None and \
          long_list != short_list:
        long_list = long_list.next
        short_list = short_list.next

    if long_list == short_list:
        return long_list
    return None

def test_prepare():
    list1 = list_util.LList(name="List1")
    for i in xrange(6):
        list1.append(i)

    list2 = list_util.LList(name="List2")
    list2.append(100)
    return (list1, list2)

def test_1():
    print "###### test 1 starts ######"
    list1, list2 = test_prepare()
    node1 = list1.get_node(2)
    node2 = list2.head
    node2.next = node1
    list1.print_list()
    list2.print_list()
    result = is_overlapping_list(list1.head, list2.head)
    if not result:
        print "Error: expected 3"
    else:
        print "Overlapping node is %d" % (result.data)
    print "###### test 1 ends ######"

def test_overlapping_list():
    test_1()

def main(argv):
    test_overlapping_list()

if __name__ == '__main__':
    main(sys.argv)
