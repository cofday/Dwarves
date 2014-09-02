__author__ = 'linweizhong'
"""
Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root == None :return  []
        result  =  []
        if root.left != None :
            result = result + self.postorderTraversal(root.left)
        if root.right != None :
            result = result + self.postorderTraversal(root.right)
        result.append(root.val)
        return  result
