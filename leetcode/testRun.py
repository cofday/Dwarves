#__author__ = 'linweizhong'
from node import  *
from postorderTraversal import  *


s = Solution()
root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root.right = n1
n1.left = n2

print s.postorderTraversal(root)







