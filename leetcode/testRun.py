#__author__ = 'linweizhong'
#from linkedListhasCycle import *
#from sortedListToBST import  *
#from maxPoints import  *
#from  copyRandomList import  *
#from  buildTreefromInorderPostorderTraversal import  *
#from  removeDuplicates import  *
#from mergeTwoLists import  *
#from  insertionSortList import  *
#from  evalRPN import *
#from  PascalTriangleII import *
from node import  *
#from   reverse import *
#from detectCycle import  *
#from longestConsecutive import  *
#from  connectBinaryTree import *
#from  generatePascalTriangle import  *
#from combine import  *
#from  maxDepth import  *
from  isBalanced import  *




s = Solution()
root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
root.left = n2
root.right = n3
n2.left = n3

print s.isBalanced(root)