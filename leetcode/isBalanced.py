__author__ = 'linweizhong'
"""
Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
class Solution:
    def balance(self,root):
        if root == None :
            return  True,0
        leftDept = rightDept = 0
        ret1 = ret2 = True
        if root.left != None:
            ret1,leftDept = self.balance(root.left)
        if root.right != None:
            ret2,rightDept = self.balance(root.right)
        if (not ret1) or (not ret2 ):
            return False,0
        if abs(leftDept - rightDept) > 1:
            return False,0
        if leftDept > rightDept :
            return  True,leftDept +1
        else:
            return True,rightDept + 1
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None :return True
        ret,maxlen=self.balance(root)
        return ret


