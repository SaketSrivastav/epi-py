#! /usr/bin/python
import sys
sys.path.append("../trees")
from binary_tree import Binary_Tree, TreeNode


def check_balanced(node):
    """
    Input: A tree node
    Output: (+)ve number if BST is balanced, otherwise -1
    Description:  Start with root node and calculate the height of the left
    subtree and right subtree. If an absolute difference of heght of left and
    right subtree is 0 or 1 then we say the tree node at N is balanced
    otherwise its unbalanced.
    """
    #Base Case
    if not node:
        return 0

    # Check if left subtree is balanced
    left_height = check_balanced(node.left)
    if left_height == -1:
        return -1

    # Check if right subtree is balanced
    right_height = check_balanced(node.right)
    if right_height == -1:
        return -1

    # If both subtree are balanced
    if abs(left_height - right_height) > 1:
        return -1

    # Return the height of node n
    return (1 + max(left_height, right_height))


def check_bst(my_bst):
    is_balanced = check_balanced(my_bst.get_root())
    return is_balanced

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


def test_1():
    print "###### test_1 starts ######"
    my_bst = test_prepare(is_bst=True)
    print "Input: "
    my_bst.inorder()
    print "\nRoot: " + str(my_bst.get_root().data)
    result = check_bst(my_bst)
    if result == -1:
        print "Error: expected balanced got unbalanced"
    else:
        print "Output: Balanced"
    print "###### test_1 ends ######"

def test_2():
    print "###### test_2 starts ######"
    my_bst = test_prepare(is_bst=False)
    print "Input: "
    my_bst.inorder()
    print "\nRoot: " + str(my_bst.get_root().data)
    result = check_bst(my_bst)
    if result != -1:
        print "Error: expected unbalanced got balanced"
    else:
        print "Output: Unbalanced"
    print "###### test_2 ends ######"


def test_check_bst():
    test_1()
    test_2()


def main(argv):
    test_check_bst()

if __name__ == '__main__':
    main(sys.argv)
