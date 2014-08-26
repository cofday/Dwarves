#__author__ = 'linweizhong'
#from linkedListhasCycle import *
#from sortedListToBST import  *
#from maxPoints import  *
#from  copyRandomList import  *
from  buildTreefromInorderPostorderTraversal import  *

from node import  *

s = Solution()

inorder  =[2,1]
postorder=[2,1]


t = s.buildTree(inorder,postorder)
t.printTree()


