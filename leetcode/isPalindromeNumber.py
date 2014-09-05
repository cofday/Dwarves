__author__ = 'linweizhong'
"""
Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
"""
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0 :return  False
        reversedNum = 0
        pn = x
        while x :
            tmp = x % 10
            reversedNum = reversedNum * 10 + tmp
            x = x / 10
        print pn ,reversedNum
        if reversedNum == pn :
            return  True
        return  False