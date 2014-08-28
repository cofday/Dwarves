__author__ = 'linweizhong'
"""
Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    def __init__(self):
        self.result = []
    def dfs(self,begin,k,n,values):
        if k == len(values) :
            tmp = [x for x in values]
            self.result.append(tmp)
            return
        print begin,k,n,values
        for i in range(begin+1,n+1):
            values.append(i)
            self.dfs(i,k,n,values)
            del  values[-1]


    # @return a list of lists of integers
    def combine(self, n, k):
        if n < 0 or k < 0 or k >n : return  self.result
        values = []
        for i in range(1,n-k+2):
            values = [i]
            self.dfs(i,k,n,values)
        return self.result





























