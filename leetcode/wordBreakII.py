__author__ = 'linweizhong'
"""
Word Break II
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
class Solution:

    def construct(self,s,dict,sentence,result):
        if len(s) == 0 :
            result.append(sentence)
            return
        for word in dict :
            if s.startswith(word) :
                if sentence == "":
                    sentence = word
                else :
                    sentence = "%s %s" %(sentence,word)
                news = s[len(word):]
                self.construct(news,dict,sentence,result)
                sentence = sentence[0:len(sentence)-len(word)]
            else:
                continue

    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        if len(s) == 0 or len(dict) == 0:return []
        result = []
        sentence = ""
        self.construct(s,dict,sentence,result)
        return  result



