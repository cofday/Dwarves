__author__ = 'linweizhong'
"""
Populating Next Right Pointers in Each Node
    Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Queue :
    def __init__(self):
        self.queue = []
    def pop(self):
        v = self.queue[0]
        del self.queue[0]
        return  v
    def add(self,x):
        self.queue.append(x)
    def size(self):
        return len(self.queue)

class Solution:
    def __init__(self):
        self.isQueue1 = True

    def clear(self,pre,isQueue1):
        pre.next = None
        pre = None
        self.isQueue1 = isQueue1
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None :return
        queue1 = Queue()
        queue2 = Queue()
        queue1.add(root)
        pre = None
        while queue1.size() != 0 or queue2.size() != 0 :
            if self.isQueue1 :
                if queue1.size() == 0 :
                    self.clear(pre,False)
                    continue
                if pre == None :
                    pre = queue1.pop()
                else :
                    n = queue1.pop()
                    pre.next = n
                    pre = n
                if pre.left != None :queue2.add(pre.left)
                if pre.right != None :queue2.add(pre.right)

            else:
                if queue2.size() == 0 :
                    self.clear(pre,True)
                    continue
                if pre == None :
                    pre = queue2.pop()
                else :
                    n = queue2.pop()
                    pre.next = n
                    pre = n
                if pre.left != None :queue1.add(pre.left)
                if pre.right != None :queue1.add(pre.right)

