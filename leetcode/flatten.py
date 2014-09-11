__author__ = 'linweizhong'
"""
 Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6


"""

from node import  *
class Solution:
    def __init__(self):
        self.result = []

    def preOrderTraver(self,root):
        if root == None : return
        self.result.append(root)
        if root.left :
            self.preOrderTraver(root.left)
        if root.right :
            self.preOrderTraver(root.right)
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root == None : return None
        self.preOrderTraver(root)
        root = self.result[0]
        p = root
        for node in self.result[1:]:
            p.right = node
            p.left = None
            p = node
        p.left = None
        p.rigt = None
        #root.printTree()





            






