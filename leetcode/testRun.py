#__author__ = 'linweizhong'
from node import  *
#from  wordBreakII import  *
#from  SingleNumber import  *
from levelOrderBottom import  *

s = Solution()
#{3,9,20,#,#,15,7}
n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
"""
n3.left = n4
n3.right = n5
"""
n1 = None
print s.levelOrderBottom(n1)







