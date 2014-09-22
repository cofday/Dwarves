__author__ = 'linweizhong'
"""

Word Break

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
class Solution:
    def sortdict(self,dict):
        lendict=[len(x) for x in dict]
        lendict.sort()

        print lendict

    def judge(self,s,dict):
        if len(s) == 0 : return True
        for item in dict :
            if s.startswith(item):
                ret = self.wordBreak(s[len(item):],dict)
                if ret : return True
        return  False
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(dict) == 0 : return  False
        self.sortdict(dict)
        #return  self.judge(s,dict)