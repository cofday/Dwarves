__author__ = 'linweizhong'
"""
Remove Element
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A) == 0 : return  0
        preidx  = 0
        nextidx = 0
        ilen = len(A)
        while nextidx < ilen  :
            if A[nextidx] == elem :
                nextidx = nextidx + 1
                continue
            A[preidx] = A[nextidx]
            preidx = preidx + 1
            nextidx = nextidx + 1
        return  preidx


