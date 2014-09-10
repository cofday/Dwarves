__author__ = 'linweizhong'
"""
Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
class Solution:
    def __init__(self):
        self.result=[]
    def findPath(self,root,sum,path):
        if root == None and sum ==0 :
            self.result.append(path)
            return
        if root == None and sum != 0 :
            return
        if root.left == None and root.right == None :
            if root.val == sum :
                path.append(root.val)
                self.result.append(path)
                return
            else:
                return
        path.append(root.val)
        if root.left != None :
            tpath=[x for x in path]
            self.findPath(root.left,sum-root.val,tpath)
        if root.right != None :
            tpath=[x for x in path]
            self.findPath(root.right,sum-root.val,tpath)

    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root == None  : return self.result
        path=[]
        self.findPath(root,sum,path)
        return  self.result


