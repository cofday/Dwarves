__author__ = 'linweizhong'
# coding:utf-8
"""
如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够N元？
"""
class Solution:
    def __init__(self):
        self.coins =[1,3,5]
    def minCountCoins(self,N):
        if N == 0 :return  0
        Min = [1000000000 for x in xrange(N+1)]
        Min[0] = 0
        for idx in xrange(1,N+1):
            for coin in self.coins :
                if idx >= coin and Min[idx -coin] + 1 < Min[idx] :
                    Min[idx] = Min[idx-coin] +1
        return Min[-1]
