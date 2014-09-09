__author__ = 'linweizhong'
"""
Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
class Solution:
    def __init__(self):
        self.isQueue1 = True
        self.queue1 = []
        self.queue2 = []
        self.result = []
        self.tmpArray = []

    def process(self,q1,q2,tag):
        if len(q1) == 0 :
            self.result.append(self.tmpArray)
            self.isQueue1 = tag
            self.tmpArray = []
            return
        cur = q1[0]
        del q1[0]
        self.tmpArray.append(cur.val)
        if cur.left != None:q2.append(cur.left)
        if cur.right != None:q2.append(cur.right)

    def levelTravel(self,root):
        if root == None :
            return
        self.queue1.append(root)
        cur = None
        while len(self.queue1) != 0  or len(self.queue2) != 0 :
            if self.isQueue1 :
                self.process(self.queue1,self.queue2,False)
            else:
                self.process(self.queue2,self.queue1,True)
        self.result.append(self.tmpArray)
        self.result.reverse()




    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        self.levelTravel(root)
        return  self.result







































