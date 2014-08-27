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
from detectCycle import  *



from node import  *

s = Solution()
head = ListNode(-1)
n1 = ListNode(1)
n2 = ListNode(2)
head.next = n1
n1.next = n2
n2.next = n1
s.detectCycle(head)
print "*****"

