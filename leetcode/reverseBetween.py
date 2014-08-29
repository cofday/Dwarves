__author__ = 'linweizhong'
"""
Reverse Linked List II
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
"""

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head  == None or n < m  or m < 1: return None
        begin = preBegin = head
        end = nextEnd = None
        pre = head
        cur = head.next
        count = 0
        while cur :
            count = count + 1
            if count < m :
                preBegin = pre
                pre = pre.next
                cur = cur.next
                begin = pre
                continue
            if count < n:
               ne = cur.next
               cur.next = pre
               pre = cur
               cur = ne
            else:
                end = pre
                nextEnd = cur
                break

        if not cur :
            if begin != head :
                preBegin.next = pre
                begin.next = None
                return head
            else:
                begin.next = None
                return pre

        if begin != head :
            preBegin.next = end
            begin.next = nextEnd
            return  head
        else :
            begin.next = nextEnd
            return end







