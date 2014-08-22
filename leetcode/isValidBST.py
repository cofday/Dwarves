# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:


    def traver(self,root,result):
	if root == None :return 
	self.traver(root.left,result)
	result.append(root.val)
	self.traver(root.right,result)
	
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
	if root ==None :return  True
	result = []
	self.traver(root,result)
	if len(result) == 1 :return True
	if len(result) == 2 :
		if result[1] > result[0] :return True
		return False
	for idx in range(1,len(result)-1):
		if result[idx]  > result[idx-1] and result[idx] < result[idx +1]:continue
		return False
	return True


n1 = TreeNode(10)
n2 = TreeNode(5)
n3 = TreeNode(15)
n4 = TreeNode(6)
n5 = TreeNode(20)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right =n5


s = Solution()
print s.isValidBST(n1)

	
