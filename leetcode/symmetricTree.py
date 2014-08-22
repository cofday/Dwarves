#!/bin/env python
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def checkSym(self,root1,root2):
	if root1 ==None and root2 == None :return True
	if root1.val != root2.val :return False
	if not self.checkSym(root1.left,root2.right):return False
	if not self.checkSym(root1.right,root2.left):return False
	return True
		

    def isSymmetric(self, root):
	if root == None :return True 
	if root.right == None and root.left == None :return True
	elif root.right != None and root.left != None :
		return self.checkSym(root.right,root.left)
	else :
		return False
		 
