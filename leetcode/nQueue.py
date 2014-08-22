class Solution:

    def __init__(self):
	self.count = 0 
	self.stack = []
	self.queuenum  = 0 

    def isSafe(self,col,row):
	for idx in range(0,col):
		if self.stack[idx]  == row  :return False
		if idx == col  : return False
		if (self.stack[idx] - idx ) == (row - col) or (self.stack[idx] + idx ) == (row + col) : return False
	return True

    def queues(self,index):
	for idx in range(self.queuenum):
		if self.isSafe(index,idx) :
			self.stack[index]=idx
			if  index == self.queuenum - 1 :
				self.count = self.count + 1
				self.stack[index]=0
				return 

			self.queues(index + 1)
	
	
	
		
    # @return an integer
    def totalNQueens(self, n):
	self.stack = [ -1 for x in range(n)]
	self.queuenum = n 
	self.queues(0)
	return self.count
		

s = Solution()
s.totalNQueens(8)
