__author__ = 'linweizhong'
"""
#Longest Consecutive Sequence
   Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

    For example,
    Given [100, 4, 200, 1, 3, 2],
    The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

    Your algorithm should run in O(n) complexity.
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if len(num) == 0 :return 0
        num = sorted(num)
        print num
        maxlen = 0
        count = 1
        for i in range(0,len(num)-1):
            print abs(abs(num[i]) - abs(num[i+1])),num[i],num[i+1]
            if abs(num[i] - num[i+1]) == 1  :
                count = count +  1
                #print count,num[i],num[i+1]
                continue
            elif num[i] == num[i+1] :
                continue
            else:
                print "******** count %d maxlen %d ******"%(count,maxlen)
                if count > maxlen :
                    maxlen = count
                count = 1
        if count > maxlen :
            maxlen = count
        return  maxlen
