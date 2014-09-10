__author__ = 'linweizhong'
"""
Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22
"""
class Solution:
    def checkPathSum(self,root,sum):
        if root == None and sum == 0 : return True
        if root == None and sum != 0 : return  False
        if root.left == None and root.right == None :
            if root.val == sum :return  True
            else:return  False

        ret1 = ret2 = False
        if root.left != None :
            ret1  = self.hasPathSum(root.left,sum-root.val)
        if root.right != None :
            ret2  = self.hasPathSum(root.right,sum-root.val)
        if ret1 or ret2 :
            return  True
        return  False
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None and sum == 0 : return False
        if root == None and sum != 0 : return  False
        return self.checkPathSum(root,sum)




















