#! /usr/bin/python
import sys
import list_util

def add_large_nos(num1, num2):
    sum_list = list_util.LList(name="Sum")
    carry = 0
    while num1 != None or num2 != None:
        local_sum = carry
        if num1 != None:
            local_sum += num1.data
            num1 = num1.next

        if num2 != None:
            local_sum += num2.data
            num2 = num2.next

        sum_list.append(local_sum % 10)
        # sum_list.print_list()
        carry = local_sum / 10
        # print "local_sum %d carry %d" % (local_sum, carry)

    if carry != 0:
        sum_list.append(carry)

    return sum_list

def test_1():
    # Add number to list in reverse order
    print "###### test_1 starts ######"
    list1 = list_util.LList(name="Num1")
    list1.append(1)
    list1.append(0)
    list1.append(0)
    list1.print_list()
    list2 = list_util.LList(name="Num2")
    list2.append(2)
    list2.append(0)
    list2.append(0)
    list2.print_list()

    sum_list = add_large_nos(list1.head, list2.head)
    sum_list.print_list()
    print "###### test_1 ends ######"

def test_2():
    # Add number to list in reverse order
    print "###### test_2 starts ######"
    list1 = list_util.LList(name="Num1")
    list1.append(0)
    list1.append(0)
    list1.append(1)
    list1.print_list()
    list2 = list_util.LList(name="Num2")
    list2.append(0)
    list2.append(0)
    list2.append(9)
    list2.print_list()

    sum_list = add_large_nos(list1.head, list2.head)
    sum_list.print_list()
    print "###### test_2 ends ######"

def test_add_large_nos():
    test_1()
    test_2()

def main(argv):
    test_add_large_nos()

if __name__ == '__main__':
    main(sys.argv)
