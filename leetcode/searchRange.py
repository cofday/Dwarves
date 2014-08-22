#!/bin/env python
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
	if len(A) == 0 :return [-1,-1]
	l = 0 
	r = len(A) - 1
	rr = -1
	lr=-1
	while l <= r :
		m = (l + r) /2
		print l,r, m
		if A[m] > target :
			r = m -1
		elif A[m] < target :
			l = m +1
		else :
			lr = rr = m 
			while lr > -1 and A[lr] == A[m]:
				lr = lr -1
			lr = lr +1
			while rr < len(A) and A[rr] == A[m]:
				rr = rr +1 
			rr = rr -1
			break
			

	return [lr,rr]
