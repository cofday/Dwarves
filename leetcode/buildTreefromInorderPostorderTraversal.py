__author__ = 'linweizhong'
from node import  *


class Solution:
    def build(self,inorder,inorderBegin,inorderEnd,postorder,postorderBegin,postorderEnd):
        if inorderBegin >  inorderEnd  :return  None
        l = r = None
        value = postorder[postorderEnd]
        root = TreeNode(value)
        index = 0
        for i in range(inorderBegin,inorderEnd +1):
            if inorder[i] == value :
                index  =  i
                break
        ilen = index - inorderBegin
        l = self.build(inorder,inorderBegin+1  ,index-1,postorder,postorderBegin,postorderBegin + ilen-1)
        r = self.build(inorder,index+1,inorderEnd,postorder,postorderBegin+ilen,postorderEnd-1)
        root.left = l
        root.right = r
        return  root

    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0 or len(postorder)==0 :return None

        return self.build(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1)

    def buildTree(self, inorder, postorder):
        if not inorder : return None
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:rootPos],postorder[])
        root.left = self.buildTree(preorder[1:rootPos+1],inorder[:rootPos])
        root.right = self.buildTree(preorder[rootPos+1:],inorder[rootPos+1:])
        return root



