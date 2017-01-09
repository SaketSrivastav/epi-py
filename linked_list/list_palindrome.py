#! /usr/bin/python
import sys
import list_util
import reverse_list

def is_list_palindrome(head):
    """
    Input: list
    Output: True is list is palindrome otherwise False
    Description: Brute force is to compare first and last, second and seconds
    last node but that is O(n^2). To do this efficiently, we can compare first
    half with reverse of second half. If they are equal then return True
    otherwise False. This is now O(n)"""
    # Skip first half
    slow = fast = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    if slow == None:
        return False

    second_half_list = list_util.LList(slow)
    first_half = head
    second_half = reverse_list.reverse_list_iterative(second_half_list)
    while second_half != None and first_half != None:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next 
    return True

def test_1():
    print "###### test_1 starts ######"
    list1 = list_util.LList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(2)
    list1.append(1)
    list1.print_list()
    result = is_list_palindrome(list1.head)
    if result == False:
        print "Error: expected True"
    else:
        print "Output: True"

    print "###### test_1 ends ######"

def test_2():
    print "###### test_2 starts ######"
    list1 = list_util.LList()
    list1.append(1)
    list1.append(2)
    list1.append(2)
    list1.append(1)
    list1.print_list()
    result = is_list_palindrome(list1.head)
    if result == False:
        print "Error: expected True"
    else:
        print "Output: True"

    print "###### test_2 ends ######"

def test_3():
    print "###### test_3 starts ######"
    list1 = list_util.LList()
    list1.append(1)
    list1.append(2)
    list1.append(0)
    list1.append(1)
    list1.print_list()
    result = is_list_palindrome(list1.head)
    if result == False:
        print "Output: False"
    else:
        print "Error: expected False"

    print "###### test_3 ends ######"

def test_list_palindrome():
    test_1()
    test_2()
    test_3()

def main(argv):
    test_list_palindrome()

if __name__ == '__main__':
    main(sys.argv)
