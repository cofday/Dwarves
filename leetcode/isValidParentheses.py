__author__ = 'linweizhong'
"""
Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution:
    def judge(self,c):
        if c == "(" or c == "{" or c == "["  :
            return  True
        else:
            return  False
    def pattern(self,c):
        if c == ")":return "("
        elif c == "}":return "{"
        elif c == "]":return "["

    # @return a boolean
    def isValid(self, s):
        if len(s) == 0 :return True
        if len(s) == 1 :return False
        stack = []
        for c in s :
            if self.judge(c) :
                stack.append(c)
                continue
            else:
                if len(stack) == 0 : return  False
                v = stack[-1]
                del stack[-1]
                if v != self.pattern(c) : return False
        if len(stack) != 0 :return False
        return  True