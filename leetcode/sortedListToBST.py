__author__ = 'linweizhong'

from node import  *
class Solution:

    def buildBST(self,array,start,end):
        if start > end : return None
        mid = (start + end) /2
        leftNode = self.buildBST(array,start,mid-1)
        parentNode = TreeNode(array[mid])

        rightNode = self.buildBST(array,mid+1,end)

        parentNode.left = leftNode
        parentNode.right = rightNode

        return  parentNode

    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head  == None :return None
        values = []
        p = head
        while p  :
            values.append(p.val)
            p = p.next
        listLen=len(values)
        return  self.buildBST(values,0,listLen)


