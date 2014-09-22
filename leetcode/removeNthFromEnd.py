__author__ = 'linweizhong'
"""
Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""
from node import  *
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None : return  None
        preNode  = head
        nextNode = head
        for idx in xrange(n):
            nextNode = nextNode.next
        if nextNode == None:
            return  head.next

        while nextNode.next :
            nextNode = nextNode.next
            preNode = preNode.next
        preNode.next = preNode.next.next
        return  head



