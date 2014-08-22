class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 :
            return ""
        pre=strs[0]
        for idx in range(1,len(strs)):
            endid=0
	    for c in pre:
		if len(strs[idx]) > endid and c == strs[idx][endid]:
			endid=endid+1
		else :
			break
	    pre=pre[0:endid]
	    if endid == 0 :
		return ""
	return pre


a=Solution()
print a.longestCommonPrefix(["a","a","a"])
