class Pair :
	def __init__(self,good,pos):
		self.good = good
		self.pos  = pos
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
	tmp = Pair(False,-1)
	stack = []
	maxlen = 0
	stack.append(tmp)
	for idx in range(len(s)):
		if s[idx] == '(' :
			tmp=Pair(True,idx)
			stack.append(tmp)
		elif s[idx] == ')':
			if len(stack) == 0 :
				tmp = Pair(False,-1)
				stack.append(tmp)
			else :
				if stack[-1].good == True :
					del stack[-1]
					if maxlen <  (idx - (stack[-1].pos)) :maxlen = (idx - (stack[-1].pos)) 
				else :
					tmp = Pair(False,idx)
					stack.append(tmp)

				
	return maxlen 

        



s = Solution()
istr="()"
print s.longestValidParentheses(istr)
