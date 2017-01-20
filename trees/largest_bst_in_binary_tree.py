#! /usr/bin/python
import sys
import binary_tree

class Minmax():
    def __init__(self):
        self.isBst = True
        self.size = 0
        self.min = float('inf')
        self.max = float('-inf')

    def __str__(self):
        return ("isBst " + str(self.isBst) + " size " + str(self.size) + \
                " min " + str(self.min) + " max " + str(self.max))

class Largest_Bst():

    def largest_bst(self, root):
        m = self.largest(root)
        return m.size

    def largest(self, node):
        """
        Input: Root node
        Output: Size of largest binary search tree in the given binary tree
        Description: Traverse tree in post order fashion. Left and right nodes
        return 4 piece of information to root which isBST, size of max BST, min and
        max in those subtree. If both left and right subtree are BST and this node
        data is greater than max of left and less than min of right then it returns
        to above level left size + right size + 1 and new min will be min of left
        side and new max will be max of right side.
        """
        if not node:
            print "Node is None"
            return Minmax()

        print "Call left_minmax of " + str(node.data)
        left_minmax = self.largest(node.left)
        print "Call right_minmax of " + str(node.data)
        right_minmax = self.largest(node.right)

        m = Minmax()
        if (left_minmax.isBst == False or \
           right_minmax.isBst == False) or \
           (left_minmax.max > node.data or \
           right_minmax.min <= node.data):
            print "Left Subtree of node (%d): %s" % (node.data, str(left_minmax))
            print "Right Subtree of node (%d): %s" % (node.data, str(right_minmax))
            m.isBst = False
            m.size = max(left_minmax.size, right_minmax.size)
            return m

        m.isBst = True
        m.size = 1 + left_minmax.size + right_minmax.size
        m.min = left_minmax.min if node.left else node.data
        m.max = right_minmax.max if node.right else node.data
        print "Node %s, Left subtree or right subtree is balanced size %s" % (str(node.data), str(m.size))
        return m
