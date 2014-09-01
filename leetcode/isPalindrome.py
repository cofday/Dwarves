__author__ = 'linweizhong'
"""
Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
class Solution:
    def isRightCharacters(self,c):
       if (c >= 'a' and c <= 'z') :
           return True
       if  (c >= '0' and c <='9'):
           return  True
       return  False
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0 :return True
        s = s.lower()
        ilen = len(s)
        leftidx = 0
        rightidx = ilen-1
        while leftidx < ilen and rightidx >= 0 :
            if not self.isRightCharacters(s[leftidx]):
                leftidx = leftidx + 1
                continue
            if not self.isRightCharacters(s[rightidx]):
                rightidx = rightidx - 1
                continue
            if s[leftidx] != s[rightidx] :
                return False
            leftidx = leftidx + 1
            rightidx = rightidx -1
        return True



