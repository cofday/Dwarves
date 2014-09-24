__author__ = 'linweizhong'
"""
Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
from node import  *
class Solution:
    def reverseLink(self,preNode,startNode,endNode):
        curNode = startNode
        nextNode = startNode.next
        while nextNode != endNode:
            tnode = nextNode.next
            nextNode.next = curNode
            curNode = nextNode
            nextNode = tnode
        preNode.next = curNode
        startNode.next = endNode
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head == None or head.next == None or k < 2: return  head

        curNode  = head
        preNode = ListNode(-1)
        preNode.next = head
        nextNode = head
        count = 0
        newhead = preNode
        while nextNode :
            if count == k :
                count = 0
                self.reverseLink(preNode,curNode,nextNode)
                preNode = curNode
                curNode = nextNode
                continue
            count = count + 1
            nextNode = nextNode.next
        if count == k :
            self.reverseLink(preNode,curNode,nextNode)
        return  newhead.next






