#!/bin/env python
from node import  *

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None :return False
        p1 = head
        p2 = p1.next
        while p1 != p2 :
            if p2 == None :return False
            if p2.next == None:return  False
            p1  = p1.next
            p2  = p2.next.next
        return True



