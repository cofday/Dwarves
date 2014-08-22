"""
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
	if n == 0 :return 1
	if n == 1 : return x
	if n == -1 :return 1/x
	m1 = n / 2
	m2 = n % 2
	v = self.pow(x,m1)
	if m2 == 1 :
		return round(v * v * x,5)
	else :
		return round(v * v,5)
		
   
"""     
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if  n == 0 :return 1
        if  n == 1 : return x 
        if  n == -1 :return 1/x
        m1 = n / 2 
        m2 = n % 2
        v = self.pow(x,m1)
        if m1 == 1 :
            return round(v*v*x,5)
        else :
            return round(v*v,5)

s = Solution()
print s.pow(34.00515,-3)
