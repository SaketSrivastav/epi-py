#! /usr/bin/python

class Check_Bst():

    def check_balanced(self, node):
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
        left_height = self.check_balanced(node.left)
        if left_height == -1:
            return -1

        # Check if right subtree is balanced
        right_height = self.check_balanced(node.right)
        if right_height == -1:
            return -1

        # If both subtree are balanced
        if abs(left_height - right_height) > 1:
            return -1

        # Return the height of node n
        return (1 + max(left_height, right_height))


    def check_bst(self, my_bst):
        is_balanced = self, self.check_balanced(my_bst.get_root())
        return is_balanced

