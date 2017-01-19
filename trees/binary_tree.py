#! /usr/bin/python
import random
import sys


class TreeNode():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree():
    def __init__(self, name="MyBST"):
        self.root = None
        self.name = name

    def get_root(self):
        return self.root

    def add(self, value=None):
        # base case
        if not self.root:
            node = TreeNode(value)
            self.root = node
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value <= node.data:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._add(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._add(node.right, value)

    def remove(self, value=None):
        if not value:
            return None

        return self._remove(self.root, value)


    def _remove(self, node, value):
        if not node:
            return node
        elif value < node.data:
            node.left = self._remove(node.left, value)
        elif value > node.data:
            node.right = self._remove(node.right, value)
        else:
            # case 1: Node has no children
            if (not node.left) and (not node.right):
                node = None
            elif not node.left:
                # case 2: Node has one child
                node = node.right
            elif not node.right:
                data = node.data
                node = node.left
            else:
                # case 3: Node has both children
                # Replace the min from right subtree of the node
                minNode = self.find_min(node.right)
                node.data = minNode.data
                node.right = self._remove(node.right, minNode.data)
        return node

    def find_min(self, node):
        if not node:
            return None

        if not node.left:
            return node
        else:
            return self.find_min(node.left)

    def search(self, value=None):
        if not value:
            return False

        if not self.root:
            return False

        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if node.data == value:
            return True
        if value < node.data:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def inorder(self):
        if not self.root:
            return
        self._inorder(self.root)

    def _inorder(self, root=None):
        if not root:
            return
        self._inorder(root.left)
        print str(root.data) + " ",
        self._inorder(root.right)

def test_add(my_bst):
    print "###### test_add begins ######"
    print "Adding: ",
    for i in [5, 3, 7, 1, 4]:
        print str(i) + " ",
        my_bst.add(value=i)
    print "\nPrinting Inorder: "
    my_bst.inorder()
    print "\nRoot: " + str(my_bst.get_root().data)
    print "###### test_add ends ######"

def test_search(my_bst):
    print "Search(%d): %r" % (5, my_bst.search(5))
    print "Search(%d): %r" % (7, my_bst.search(8))
    print "Search(%d): %r" % (0, my_bst.search(0))

def test_remove(my_bst):
    print "Remove(%d): %r" % (7, my_bst.remove(7) != None)
    print "Printing Tree:"
    my_bst.inorder()

    print "\nRemove(%d): %r" % (3, my_bst.remove(3) != None)
    print "Printing Tree:"
    my_bst.inorder()

def test_binary_tree():
    my_bst = Binary_Tree("bst_1")
    test_add(my_bst)
    test_search(my_bst)
    test_remove(my_bst)

def main(argv):
    test_binary_tree()

if __name__ == '__main__':
    main(sys.argv)
