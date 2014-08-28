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
from  connectBinaryTree import *


s = Solution()
root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(6)

root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5


s.connect(root)
print n3.next.next.val
