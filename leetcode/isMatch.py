__author__ = 'linweizhong'
# coding:utf-8
"""
Regular Expression Matching
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

"""
class Solution:
    # @return a boolean
    # Time Limit Exceeded
    def isMatch1(self, s, p):
        if len(p) == 0 :return len(s) == 0
        if len(p) == 1 :
            if p[0] == "*":return True
            if len(s) != 1 : return  False
            if s[0] != p[0] and p[0] !="." : return False
            return True
        if p[1] != "*" :
            if len(s) ==0 : return False
            if p[0] != s[0] and p[0] != "." : return  False
            return self.isMatch(s[1:],p[1:])
        else:
            idx = -1
            ilen = len(s)
            while idx < ilen and (idx < 0 or p[0] == s[0] or p[0] == "."):
                if self.isMatch(s[idx+1:],p[2:]):return True
                idx = idx +1
            return  False
    #from internet
    #some useful page :
    #http://www.cnblogs.com/Anker/archive/2013/03/15/2961725.html
    #http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=dynProg
    #http://hawstein.com/posts/dp-novice-to-advanced.html
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]










