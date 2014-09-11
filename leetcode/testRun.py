#__author__ = 'linweizhong'
from node import  *
#from  wordBreakII import  *
#from  SingleNumber import  *
from flatten import  *
s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

n1.left = n2
n1.right = n5
n2.left = n3
n2.right = n4
n5.right = n6


s.flatten(n1)






