#!/bin/evn python
class TreeNode :
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def traver(self,root,result):
		if root == None :return
		result.append(root.val)
		if root.left != None :self.traver(root.left,result)
		if root.right != None :self.traver(root.right,result)

	
	def preorderTraversal(self, root):
		result = []
		if root == None :return result
		self.traver(root,result)
		print result
		return result
		

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.left = n2
n2.right = n3

s = Solution()
s.preorderTraversal(n1)
