__author__ = 'linweizhong'
"""
Single Number II
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


"""
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A) == 0 :
            return None
        ones = twos = threes = 0
        for i in range(len(A)):
            threes = twos  &  A[i]
            twos = twos | ones & A[i]
            ones = ones | A[i]

            twos = twos &  ~threes
            ones = ones & ~threes
        return  ones


