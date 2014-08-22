#!/bash/env python

class Solution:

    def	findsets(self,S,R):
	if len(S) == 0 :return 
	v = S[0]
	for s in R :
		if s == [] :
			R.append([v])
		else :
			if v > s[-1]:
				tmpResult = [x for x in s]
				tmpResult.append(v)
				R.append(tmpResult)
		
	del S[0]
	return self.findsets(S,R)

    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
	result = []
	result.append([])
	self.findsets(S,result)
	print result


		
