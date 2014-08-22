#!/bin/env python
class ListNode :
	def __init__(self,x):
		self.val=x
		self.next=None

	def printList(self):
		n=self
		while n !=None :
			print n.val
			n=n.next
		



class Solution :
	def deleteDuplicates(self,head):
		if head == None :
			return None
		values = [head.val]
		node1 = head
		node2 = head.next 
		while node2  != None:
			if node2.val not in values:
				values.append(node2.val)
				node1 = node2
				node2 = node2.next
				continue
			if node2.next == None :
				node1.next=None
				return head 
			#elif node2.next.next ==None :
			#	node1.next=node2.next
			#	node2=node2.next
			else :
				node1.next = node2.next
				node2 = node2.next
		return head  


		
		



head=ListNode
l1=ListNode(2)
l2=ListNode(2)
#l3=ListNode(2)
#l4=ListNode(2)

l1.next = l2
#l2.next = l3
#l3.next = l4
l1.printList()
print "************"
a=Solution()
a.deleteDuplicates(l1)
l1.printList()

