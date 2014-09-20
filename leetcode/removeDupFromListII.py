__author__ = 'linweizhong'
"""

Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node import *
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None : return head
        nodes = {}
        cur  = head
        while cur:
            if nodes.has_key(cur.val):
                nodes[cur.val] = 1
            else:
                nodes[cur.val] = 0
            cur = cur.next

        cur = head
        while cur :
            if nodes[cur.val] == 0 : break
            cur = cur.next
        head = pre = cur

        if cur == None or cur.next == None   : return  head
        cur = cur.next
        pre.next = None
        head.printList()
        while cur :
            print cur.val,nodes[cur.val]
            if nodes[cur.val] == 1 :
                cur = cur.next
                continue
            pre.next = cur
            pre  = cur
            cur = cur.next
        if pre.next != None : pre.next = None
        return  head








