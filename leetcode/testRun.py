#__author__ = 'linweizhong'
#from linkedListhasCycle import *
#from sortedListToBST import  *
#from maxPoints import  *
from  copyRandomList import  *
from node import  *

head = RandomListNode(-1)
n2 = RandomListNode(-1)
#n1.next = n2
#n1.random = n1
s = Solution()
t =  s.copyRandomList(head)
while t :
    print t.label
    t = t.next

