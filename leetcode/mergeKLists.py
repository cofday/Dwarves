__author__ = 'linweizhong'
#coding:utf-8
"""
Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
为啥leetcode 不让用python的库呢 java都行，歧视啊
这边用了3中方法：
1.merge Two list 用了递归  AC
2.用了Priority Queue  leetcode 不支持 import的代码,是想让提交者自己写吗？
3.最土的，每次遍历一次lists，得到最小的插入最终的表中 time limit exceeded了

"""
from node import  *
from Queue import  PriorityQueue
class PriorityNode :
    def __init__(self,priority,node):
        self.priority = priority
        self.ListNode = node
    def __cmp__(self, other):
        return cmp(self.priority,other.priority)
class Solution:
    def mergeTwoList(self,head1,head2):
        if head1 == None and head2 == None : return None
        elif head1 !=None and head2 == None : return  head1
        elif head1 == None and head2 != None : return  head2

        head = head1
        if head1.val > head2.val:
            head = head2
            head2 = head2.next
        else:
            head1 = head1.next
        tail = head
        while head1 and head2 :
            if head1.val < head2.val :
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1 :
            tail.next = head1
        elif head2 :
            tail.next = head2
        return  head
   # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) == 0 : return  None
        elif len(lists) == 1 : return  lists[0]
        elif len(lists) == 2 : return self.mergeTwoList(lists[0],lists[1])
        else:
            #print len(lists)/2
            return  self.mergeTwoList(self.mergeKLists(lists[0:len(lists)/2]),
                                     self.mergeKLists(lists[len(lists)/2:])
                                    )

    def mergeKLists2(self, lists):
        if len(lists) == 0 : return  None
        if len(lists) == 1 : return  lists[0]
        pq = PriorityQueue()
        for idx in xrange(len(lists)):
            if lists[idx] != None :
                pq.put(PriorityNode(lists[idx].val,lists[idx]))

        dump = ListNode(-1)
        tail = dump
        while not  pq.empty():
            tail.next = pq.get().ListNode
            tail = tail.next
            if tail.next != None:
                pq.put(PriorityNode(tail.next.val,tail.next))
        return dump.next




    def mergeKLists1(self, lists):
        if len(lists) == 0 :
            return  None
        if len(lists) == 1 :
            return lists[0]
        k = len(lists)-1
        preNode = ListNode(-1)
        head = preNode
        while True  :
            tnode = lists[0]
            offset = 0
            for idx in xrange(1,len(lists)):
                if lists[idx] == None :
                    continue
                if tnode == None :
                    tnode = lists[idx]
                    offset = idx
                else:
                    if lists[idx].val < tnode.val :
                        tnode = lists[idx]
                        offset = idx

            if tnode == None :
                break
            preNode.next = tnode
            preNode = tnode
            lists[offset] = lists[offset].next

        return  head.next



