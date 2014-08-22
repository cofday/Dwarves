class Solution:

    def judge(self,l,r):
	if r == "V" or r == "X":
		if l != "I":return -1
	if r == "L" or r == "C":
		if l != "X" :return -1
	if r == "D" or r == "M" :
		if l != "C" :return -1
	return 0
	
    # @return an integer
    def romanToInt(self, s):
	romanMap={
		"I":1,
		"V":5,
		"X":10,
		"L":50,
		"C":100,
		"D":500,
		"M":1000
	}

	value = 0
	idx = 0
	while idx < len(s) :
		if idx < len(s)-1: 
			l = s[idx]
			r = s[idx+1]
			vl = romanMap[l]
			vr = romanMap[r]
			if vr > vl :
				if self.judge(vl,vr) != 0 :return -1
				value = value + vr - vl 
				idx = idx + 2
			else :
				value = value + vl
				idx = idx +1
		else :
			value = value + romanMap[s[idx]]
			idx = idx +1
		

	return value
			


