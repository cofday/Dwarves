#__author__ = 'linweizhong'
from node import  *
from mergeKLists import  *

s = Solution()
l1 = Link([])
l2 = Link([1])
#l3 = Link([92,84,75,274,39847])
#lists =[l1.head,l2.head,l3.head]
lists =[l1.head,l2.head]
l=  s.mergeKLists1(lists)
l.printList()

m1 = Link([])
m2 = Link([1])
#m3 = Link([92,84,75,274,39847])
#ms =[m1.head,m2.head,m3.head]
ms =[m1.head,m2.head]
m = s.mergeKLists(ms)
m.printList()



