# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
	if p.val != q.val :return False
	if p.left != None and q.left != None :
		if self.isSameTree(p.left,q.left) == False :return False
	elif not (p.left == None  and  q.left == None) :return False

	if p.right != None and q.right != None :
		if self.isSameTree(p.right,q.right)==False : return False
	elif not(p.right == None and q.right == None) : return False

	
	return True        


