__author__ = 'linweizhong'
"""
Interleaving String
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aa dbbc bc a c", return true.
When s3 = "aa dbbbaccc", return false.
"""
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        s = s1[::-1]
        news = s + s2 + s
        print news
        print s3
        if s3 in news : return  True
        s = s2[::-1]
        news = s + s1 + s
        if s3 in news : return  True

        return  False
