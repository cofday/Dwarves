__author__ = 'linweizhong'
from node import  *
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None :return  l2
        elif l2 == None :return l1
        else:
            head =None
            p = None
            if l1.val > l2.val :
                p = l2
                l2 = l2.next
            else :
                p = l1
                l1 = l1.next
            head = p
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2  = l2.next
                p = p.next
            if l1 != None:
                p.next = l1
            if l2 != None :
                p.next = l2
            return  head
