__author__ = 'linweizhong'
"""
Pascal's Triangle Total Accepted: 17483 Total Submissions: 55219 My Submissions
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
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
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0 :return  []
        if numRows == 1 :return [[1]]
        result = [[1],[1,1]]
        queue  = Queue(numRows)
        queue.add(1)
        queue.add(1)
        for index in range(1,numRows-1):
            v1 =  v2 = 0
            for idx in range(index+1):
                v1 = v2
                v2 = queue.pop()
                v = v1 + v2
                queue.add(v)
            queue.add(1)
            oneline = [x for x in queue.queue[:queue.index]]
            result.append(oneline)

        return  result

