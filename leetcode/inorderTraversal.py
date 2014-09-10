__author__ = 'linweizhong'
"""
Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""
class Solution:
    def __init__(self):
        self.stack = []
    def findleftLeaf(self,root):
        cur = root
        while cur :
            self.stack.append(cur)
            cur = cur.left
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:return []
        result = []
        cur = root
        self.findleftLeaf(root)
        while len(self.stack) != 0 :
            cur = self.stack[-1]
            del self.stack[-1]
            result.append(cur.val)
            if cur.right != None:
                self.findleftLeaf(cur.right)
        return  result




