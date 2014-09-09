#__author__ = 'linweizhong'
from node import  *
#from  wordBreakII import  *
#from  SingleNumber import  *
from  maxPathSum import  *
s = Solution()
n1 = TreeNode(2)
n2 = TreeNode(-1)
n3 = TreeNode(1)
n4 = TreeNode(20)
n5 = TreeNode(20)
n1.left= n2
#n1.right = n3
#n2.left = n4
#n2.right = n5
print s.maxPathSum(n1)





