__author__ = 'linweizhong'
"""
Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
class Solution:
    def __init__(self):
        self.path = None

    def maxValue(self,root):
        if root == None : return  0
        leftValue = rightValue = 0
        if root.left != None :
            leftValue = self.maxValue(root.left)
            if leftValue < 0 :leftValue = 0
        if  root.right != None:
            rightValue = self.maxValue(root.right)
            if rightValue < 0 :rightValue = 0

        newpath = rightValue + leftValue + root.val

        if self.path==None or self.path < newpath :
            self.path = newpath

        if leftValue > rightValue :
            return  leftValue + root.val
        else:
            return  rightValue + root.val
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxValue(root)
        return self.path




