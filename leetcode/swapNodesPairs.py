#!/bin/env python
class ListNode :
	def __init__(self,x):
		self.val=x
		self.next=None

	def printList(self):
		print self.val
		node = self.next
		while node !=None :
			print node.val
			node = node.next
			
		



class Solution :
	def swapPairs(self, head):
		if head == None :return head
		h = ListNode(-1)
		h.next = head 
		m = head 
		if m.next == None : return head 
		l =  m.next
		head = h
		while 1 :
			print "m val",m.val
			print "l val",l.val
			print "h val",h.val
			h.next = l
			m.next = l.next
			l.next = m
			if m.next  == None  or m.next.next == None :break
			h = l.next 
			m = h.next
			l = m.next
		return head.next 




