__author__ = 'linweizhong'
"""

Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

pre
ABDECF
12
inodor
DBEAFC
21
"""
from  node import  *

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not inorder : return None
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootPos+1],inorder[:rootPos])
        root.right = self.buildTree(preorder[rootPos+1:],inorder[rootPos+1:])
        return root


