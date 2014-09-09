__author__ = 'linweizhong'
"""
Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
from  node import  *
class Solution:
    def build(self,num,begin,end):
        if begin > end :return  None
        mid = (begin + end) / 2
        value = num[mid]
        parentNode = TreeNode(value)
        leftNode = self.build(num,begin,mid-1)
        rightNode = self.build(num,mid+1,end)
        parentNode.left  = leftNode
        parentNode.right = rightNode
        return  parentNode

    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0 :return  None
        return  self.build(num,0,len(num)-1)


