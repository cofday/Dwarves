__author__ = 'linweizhong'
"""
#   Linked List Cycle II
#       Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
"""

class Solution:
    def hasCycle(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast :break
        if slow != fast :
            return  False,None
        else:
            return True,fast

    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None or head.next == None :return None
        ret,meetNode = self.hasCycle(head)
        if not ret :
            return  None
        else:
            startNode = head
            while meetNode != startNode :
                meetNode = meetNode.next
                startNode = startNode.next
            return startNode