#!/bin/env python
import sys
import os

class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

	
			

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
	if root == None :
		return []
        isEven = 1 
        evenQueue = []
        oddQueue = []  
        allResult = []
        evenQueue.append(root)
        onelevel = []
        
        while len(evenQueue) != 0 or len(oddQueue) != 0:
            queue=evenQueue
            if isEven == 1 :
                queue=evenQueue
            else :
                queue=oddQueue
                
            if len(queue) != 0 :
                node = queue[0]
                del queue[0]
            else :
                if isEven == 0 :
                    onelevel.reverse()
                    isEven = 1
                else :
                    isEven = 0
                allResult.append(onelevel)
                onelevel = []
                continue
            value = node.val
            onelevel.append(value)
            queue=oddQueue
            if isEven == 1 :
                queue=oddQueue
            else:
                queue=evenQueue
            if node.left != None:queue.append(node.left)
            if node.right != None:queue.append(node.right)
	print isEven
        if isEven == 0 :onelevel.reverse()
        allResult.append(onelevel)
	print allResult
        return allResult




