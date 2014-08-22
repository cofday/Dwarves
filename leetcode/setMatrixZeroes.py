class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
	for a in matrix:
		print a
	print "************"
	if len(matrix) == 0 :return matrix
        mlen = len(matrix[0])
        nlen = len(matrix)
	m = [1 for x in range(mlen)]
	n = [1 for x in range(nlen)]
	for nidx in range(nlen):
		for midx in range(mlen):
			if matrix[nidx][midx] == 0 :
				m[midx] = 0
				n[nidx] = 0
				continue
	for nidx in range(nlen) :
		for midx in range(mlen):
			if m[midx] == 0 or n[nidx] == 0 :
				matrix[nidx][midx] = 0 
	for a in matrix :
		print a
        


