__author__ = 'linweizhong'
"""
Reorder List
Given a singly linked list L: l0 -> l1 -> l2 ... ln-1 -> ln
reorder it to: l0 -> ln -> l2 -> ln-1
You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
class Solution:
    def reversed(self,l):
        preNode = l
        nextNode = l.next
        preNode.next = None
        while nextNode :
            ne = nextNode.next
            nextNode.next = preNode
            preNode = nextNode
            nextNode = ne

        return preNode

    def merge(self,l1,l2):
        p1 = l1
        p2 = l2
        while p1 and p2 :
            ne1 = p1.next
            ne2  = p2.next
            p1.next = p2
            p2.next = ne1
            p1 = ne1
            p2 = ne2
        return l1

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next ==None :return head
        fast = head
        slow = head
        while fast and fast.next and fast.next.next :
            fast = fast.next.next
            slow = slow.next
        l1 = head
        l2 = slow.next
        slow.next = None
        l2 = self.reversed(l2)
        l1.printList()
        l2.printList()
        head = l1
        self.merge(head,l2)
        return head





