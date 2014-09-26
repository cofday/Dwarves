__author__ = 'linweizhong'
"""
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
class Solution:

    def buildParenthesis(self,leftNum,rightNum,result,istr):
        if leftNum == 0 and rightNum == 0 :
            result.append(istr)
        if leftNum > 0 :
            self.buildParenthesis(leftNum-1 , rightNum,result,istr+"(")
        if rightNum > 0 and leftNum < rightNum :
            self.buildParenthesis(leftNum,rightNum-1,result,istr+")")

    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0 : return [""]
        result = []
        self.buildParenthesis(n,n,result,"")
        return  result



