__author__ = 'linweizhong'
from node import  *


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder : return None
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:rootPos],postorder[:rootPos])
        root.right = self.buildTree(inorder[rootPos+1:],postorder[rootPos:-1])
        return root



