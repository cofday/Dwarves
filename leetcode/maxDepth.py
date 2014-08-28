__author__ = 'linweizhong'
"""
Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
from node import  *
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:return 0
        leftdepth = 0
        rightdepth = 0
        if root.left != None :
            leftdepth = self.maxDepth(root.left)
        if root.right != None :
            rightdepth = self.maxDepth(root.right)
        if leftdepth > rightdepth :
            return  1 + leftdepth
        else:
            return 1 + rightdepth

