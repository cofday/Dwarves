class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
	if len(A) == 0 :return 0
	l = 0
	r = len(A)-1
	m = 0
	while l <= r :
		m = (l + r )/2
		mv = A[m]
		if mv > target :
			r = m -1 
		elif mv < target :
			l = m +1
		else :
			return m
	if A[m]	 > target :return m 
	else :return m +1


