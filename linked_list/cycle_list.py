#! /usr/bin/python
import sys
import list_util

def has_cycle(head):
    """
    Input: list head node of which we need to run cyclicity test
    Output: the node in the list where there is a cycle or -1 if no cycle
    Description: This algorithm has 2 stages, detecting a cycle and find the
        cycle node.
        To detect the cycle we have slow and fast pointers. Slow
        increments by 1 and fast increments by 2. If there is a cycle slow
        catches up to fast. If slow is equal to fast at any instant the there
        is a cycle in the list.
        To find the cycle node, we first calculate cycle length by moving one
        of the pointer slow/fast to calculate the length. We then keep one
        iterator to head and another iterator cycle length away from it. We
        continue to traverse the list untill they meet. The node where they
        meet is the node where the cycle begins.
    """
    slow = head
    fast = head
    while fast.next != None and \
          fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Detected a cycle
            print "Cycle found"
            fast = fast.next
            cycle_len = 1
            while(fast != slow):
                cycle_len += 1
                fast = fast.next
            print "Cycle length: %d" % (cycle_len)
            if cycle_len == 0:
                return None
            # Move new iter cycle length away from head
            new_iter = head
            while cycle_len > 0:
                new_iter = new_iter.next
                cycle_len -= 1
            new_iter1 = head
            # Move new_iter and new_iter1 consecutively to find the cycle node
            while new_iter != None and \
                  new_iter1 != None and \
                  new_iter != new_iter1:
                new_iter = new_iter.next
                new_iter1 = new_iter1.next
            if new_iter1 == new_iter:
                return new_iter
    return None

def test_prepare():
    list1 = list_util.LList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.print_list()
    return list1

def test_1():
    print "##### Test 1 starts #####"
    list1 = test_prepare()
    head1 = list1.head
    sec_node = list1.get_node(1)
    fourth_node = list1.get_node(3)
    fourth_node.next = sec_node
    print "Created cycle between %d and %d" % (sec_node.data, fourth_node.data)
    cycle = has_cycle(list1.head)
    if cycle != None:
        print "Output: cycle node: " + str(cycle.data)
    else:
        print "Error: expected cycle node 2 but got None"
    print "##### Test 1 ends #####"

def test_2():
    print "##### Test 2 starts #####"
    list1 = test_prepare()
    head1 = list1.head
    first_node = list1.head
    fourth_node = list1.get_node(3)
    fourth_node.next = first_node
    print "Created cycle between %d and %d" % (first_node.data, fourth_node.data)
    cycle = has_cycle(list1.head)
    if cycle != None:
        print "Output: cycle node: " + str(cycle.data)
    else:
        print "Error: expected cycle node 2 but got None"
    print "##### Test 2 ends #####"

def test_3():
    print "##### Test 3 starts #####"
    list1 = test_prepare()
    head1 = list1.head
    fourth_node = list1.get_node(3)
    fourth_node.next = fourth_node 
    print "Created cycle between %d and %d" % (fourth_node.data, fourth_node.data)
    cycle = has_cycle(list1.head)
    if cycle != None:
        print "Output: cycle node: " + str(cycle.data)
    else:
        print "Error: expected cycle node 2 but got None"
    print "##### Test 3 ends #####"

def test_has_cycle():
    test_1()
    test_2()
    test_3()

def main(argv):
    test_has_cycle()

if __name__ == '__main__':
    main(sys.argv)
