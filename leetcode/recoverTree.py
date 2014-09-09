__author__ = 'linweizhong'
"""
Recover Binary Search Tree
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

"""
class Solution:
    def __init__(self):
        self.mistake1 = None
        self.mistake2 = None
        self.pre = None

    def orderTravel(self,root):
        if root == None :return

        if root.left != None:
            self.orderTravel(root.left)
        if self.pre != None and root.val < self.pre.val:
            if self.mistake1 == None:
                self.mistake1 = self.pre
                self.mistake2 = root
            else :
                self.mistake2 = root
        self.pre = root

        if root.right != None:
            self.orderTravel(root.right)



    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.orderTravel(root)
        if self.mistake1 != None and self.mistake2 != None :
            tmp = self.mistake1.val
            self.mistake1.val = self.mistake2.val
            self.mistake2.val = tmp
        return  root





