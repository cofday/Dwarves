__author__ = 'linweizhong'
from  node import  *

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:return None
        p = head
        while p :
            newNode = RandomListNode(p.label)
            newNode.next  = p.next
            p.next = newNode
            p = newNode.next
        print head.label
        p1 = head
        p2 = head.next
        while p2 :
            if p1.random != None:
                p2.random = p1.random.next
            else:
                p2.random  = None
            if p2.next == None:break
            p1 = p2.next
            p2 = p1.next
        res = head.next
        p1 = head
        p2 = p1.next
        while p2.next :
            p1.next = p1.next.next
            p2.next = p2.next.next
            if p2.next == None :break
            p1  = p1.next
            p2 = p2.next
        p2.next = None
        p1.next = None
        return  res

