__author__ = 'linweizhong'
# -*- coding: utf-8 -*-
"""
Distinct Subsequences
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""
class Solution:
    def __init__(self):
        self.count = 0
    #这种解法，超时
    def distinctStat1(self,S,T):
        if len(S) < len(T): return
        if len(S) == 0 and len(T) != 0 :
            return
        if len(T) == 0 and len(S) >= 0 :
            self.count = self.count + 1
            return
        v = T[0]
        for idx in range(len(S)) :
            if v != S[idx] :
                continue
            if (len(T[1:])) > len(S[idx+1:]):
                break
            self.distinctStat(S[idx+1:],T[1:])
            #10582116


    def distinctStat(self,S,T):
        lenS = len(S)
        lenT = len(T)

    # @return an integer
    def numDistinct(self, S, T):
        self.distinctStat1(S,T)
        return self.count