__author__ = 'linweizhong'
"""
Sort List
Sort a linked list in O(n log n) time using constant space complexity.
"""
from  node import  *
class Solution:

    def findMidNode(self,head):
        if (not head) or (not head.next ) : return  head
        fast = head
        slow = head
        while fast and fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self,l1,l2):
        head = TreeNode(-1)
        tail = head
        while l1 and l2 :
            if l2.val > l1.val :
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2  = l2.next
            tail = tail.next
        if l1 :
            tail.next = l1
        if l2 :
            tail.next  = l2
        return head.next


    def mergeSort(self,head):
        if (not head ) or (not head.next ):return head
        mid = self.findMidNode(head)
        right = mid.next
        left = head
        mid.next = None
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return  self.merge(left,right)

    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None :return head
        return self.mergeSort(head)





