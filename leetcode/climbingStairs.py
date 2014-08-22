#!/bin/env python

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
	if n < 4 :
		return n
	a = 2 
	b = 3
	c = 5
	for i in range(5,n+1):
		a = c 
		c = b + c
		b = a
	return c
		


s = Solution()
print s.climbStairs(10)
