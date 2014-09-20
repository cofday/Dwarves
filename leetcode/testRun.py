#__author__ = 'linweizhong'
from node import  *
from  removeDupFromListII import  *

s = Solution()
head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(2)
n5 = ListNode(3)
n6 = ListNode(4)

head.next = n1
n1.next = n2
n2.next = n3
#n3.next = n4
#n4.next = n5
#n5.next = n6
head.printList()

l = s.deleteDuplicates(head)
print l
l.printList()







