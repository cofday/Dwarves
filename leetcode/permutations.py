#!/bin/env python
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
	if len(num) == 0 :return []
	result = [[]]
	ilen =  -1 
	for obj in num :
		ilen = ilen + 1
		while 1  :
			attr = result[0]
			if len(attr) > ilen :break
			for idx in range(len(attr)+1):
				tmp = [x for  x in attr]
				tmp.insert(idx,obj)
				result.append(tmp)
			result.remove(attr)
		

	print result
				
		
		
	
	

s = Solution()
num  = [1]
s.permute(num)
