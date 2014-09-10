__author__ = 'linweizhong'
"""
Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
class Solution:
    # @param root, a tree node
    # @return an integer

    def minDepth(self,root):
        if root == None :return  0
        elif root.left == None and root.right == None :return  1
        else:
            l =  r = 0
            if root.left != None :
                l = self.minDepth(root.left)
            if root.right != None:
                r = self.minDepth(root.right)
            if l == 0 and r != 0 :
                return  r +1
            elif r == 0 and l != 0 :
                return l+1
            if l > r :
                return  r + 1
            else:
                return  l + 1


