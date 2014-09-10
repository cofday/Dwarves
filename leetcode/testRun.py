#__author__ = 'linweizhong'
from node import  *
#from  wordBreakII import  *
#from  SingleNumber import  *
from  minDepth import  *
s = Solution()
root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(1)
n4 =  TreeNode(1)
n5 = TreeNode(1)
"""
root.left = n1
root.right = n2
n2.left = n3
n1.right = n4

root.left = n1
n1.left = n2
n2.left = n3
n3.left =
"""
root.left = n1
print s.minDepth(root)
"""
from isInterleave import  *
s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print s.isInterleave(s1,s2,s3)
"""
"""
from buildTreefromInorderPostorderTraversal import  *
s = Solution()
A = ["D","B","E","A","F","C"]
B = ["D","E","B","F","C","A"]
A = [2,1]
B = [2,1]
t= s.buildTree(A, B)
t.printTree()
"""





