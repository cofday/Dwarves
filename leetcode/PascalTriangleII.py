__author__ = 'linweizhong'
"""
#Pascal's Triangle II
#   Given an index k, return the kth row of the Pascal's triangle.
#   For example, given k = 3,Return [1,3,3,1].
#   Note :
#       Could you optimize your algorithm to use only O(k) extra space?
"""
class Queue :
    def __init__(self,size):
        self.size = size
        self.queue = [0 for x in range(size+1)]
        self.index = 0
    def add(self,x):
        if self.index <= self.size :
            self.queue[self.index]  = x
            self.index = self.index + 1

    def pop(self):
        v = self.queue[0]
        for i in range(1,self.index):
            self.queue[i-1] = self.queue[i]
        self.index = self.index-1
        return v


class Solution:
    # @return a list of integers
    def getRow1(self, rowIndex):
        if rowIndex == 0 :return  [1]
        result = [1,1]
        for index in range(1,rowIndex):
            newResult=[1]
            for idx in range(1,len(result)):
                newResult.append(result[idx] + result[idx-1])
            newResult.append(1)
            result = newResult
        return  result
    #just  use only O(k) extra space
    def getRow(self,rowIndex):
        if rowIndex ==  0 :return  [1]
        queue = Queue(rowIndex)
        queue.add(1)
        queue.add(1)
        for index in range(1,rowIndex):
            v1 =  v2 = 0
            for idx in range(index+1):
                v1 = v2
                v2 = queue.pop()
                v = v1 + v2
                queue.add(v)
            queue.add(1)

        return queue.queue







