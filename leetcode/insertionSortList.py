__author__ = 'linweizhong'
from node import  *
class Solution:
    def findRightPos(self,head,p):
        pre = head
        next = head.next
        while next and p.val >= next.val:
            pre = next
            next = next.next
        return  pre

    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None:return  head
        newHead = ListNode(-1)
        while head :
            next = head.next
            pre = self.findRightPos(newHead,head)
            new_next = pre.next
            pre.next = head
            head.next = new_next
            head = next
        return newHead.next


