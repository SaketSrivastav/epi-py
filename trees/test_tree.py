import sys
import pytest
from binary_tree import Binary_Tree
from check_bst import Check_Bst
from largest_bst_in_binary_tree import Largest_Bst

def test_prepare(is_bst=True):
    my_bst = Binary_Tree("BST_1")
    if is_bst:
        my_bst.add(5)
        my_bst.add(3)
        my_bst.add(7)
        my_bst.add(1)
        my_bst.add(4)
        my_bst.add(6)
        my_bst.add(8)
    else:
        my_bst.add(3)
        my_bst.add(1)
        my_bst.add(4)
        my_bst.add(5)
        my_bst.add(6)
        my_bst.add(8)

    return my_bst


def test_check_bst_1():
    print "\n###### test_check_bst_1 starts ######"
    my_bst = test_prepare(is_bst=True)
    print "Input: "
    my_bst.inorder()
    print "\nRoot: " + str(my_bst.get_root().data)
    result = Check_Bst().check_bst(my_bst)
    assert result != -1
    print "Output: Balanced"
    print "\n###### test_check_bst_1 ends ######"

def test_check_bst_2():
    print "\n###### test_check_bst_2 starts ######"
    my_bst = test_prepare(is_bst=False)
    print "Input: "
    my_bst.inorder()
    print "\nRoot: " + str(my_bst.get_root().data)
    result = Check_Bst().check_bst(my_bst)
    if result != -1:
        print "Error: expected unbalanced got balanced"
    else:
        print "Output: Unbalanced"
    print "\n###### test_check_bst_2 ends ######"

def test_largest_bst_in_binary_tree_positive_1():
    print "###### test_largest_bst_in_binary_tree_positive_1 starts ######"
    my_bst = test_prepare(is_bst=True)
    print "Input: "
    my_bst.inorder()
    print "\nRoot: " + str(my_bst.get_root().data)
    result = Largest_Bst().largest_bst(my_bst.get_root())
    print "Max Size: " + str(result)
    assert result == 7
    print "###### test_largest_bst_in_binary_tree_positive_1 ends ######"

def test_largest_bst_in_binary_tree_negative_1():
    print "###### test_largest_bst_in_binary_tree_negative_1 starts ######"
    my_bst = test_prepare(is_bst=False)
    print "Input: "
    my_bst.inorder()
    print "\nRoot: " + str(my_bst.get_root().data)
    result = Largest_Bst().largest_bst(my_bst.get_root())
    print "Max Size: " + str(result)
    assert result == 6
    print "###### test_largest_bst_in_binary_tree_negative_1 ends ######"
