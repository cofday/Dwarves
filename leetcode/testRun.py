#__author__ = 'linweizhong'
#from linkedListhasCycle import *
#from sortedListToBST import  *
#from maxPoints import  *
#from  copyRandomList import  *
#from  buildTreefromInorderPostorderTraversal import  *
#from  removeDuplicates import  *
#from mergeTwoLists import  *
#from  insertionSortList import  *
from  evalRPN import *

from node import  *

s = Solution()
token =  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print s.evalRPN(token)




























"""
n1 = ListNode(-1)
n2 = ListNode(3)
n3 = ListNode(2)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
#n2.next = n5
n = s.insertionSortList(n1)
#n= s.mergeTwoLists(n1,n2)
n.printList()


A=[1]
print s.removeDuplicates(A)

inorder  =[2,1]
postorder=[2,1]


t = s.buildTree(inorder,postorder)
t.printTree()
"""


