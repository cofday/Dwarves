#!/bin/evn python
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

endNode=ListNode(1)
class Solution:	
    def adjust(self,l):
	p = l 
	while l != None :
		if l.val == 9 :
			l.val = 0 
		elif l.val >= 10 :
			l.val = l.val % 10 
		else :
			l.val = l.val + 1
			break
		p = l 
		l = l.next
	if l == None :
		p.next = endNode

    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
	p1 = l1
	p2 = l2
	p3 = l1
	carry = 0 
	while p1 != None and p2 != None :
		value = p1.val + p2.val + carry
		if value >= 10 :
			value = value % 10 
			carry = 1 
		else :
			carry = 0 
		p1.val = value
		p3 = p1
		p1 = p1.next
		p2 = p2.next
	if p1 != None :
		if carry != 0 :
			self.adjust(p1)	
		
	elif p2 != None :
		p3.next = p2
		if carry != 0 :
			self.adjust(p2)
	else :
		if carry != 0 :
			p3.val = p3.val + 10 
			self.adjust(p3)
	return l1
			

