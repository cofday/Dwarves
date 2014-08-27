__author__ = 'linweizhong'
"""
#
# Evaluate Reverse Polish Notation
#   Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#   Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#   Some examples:
#       ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#       ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
class Solution:
    def isNum(self,token):
        try:
            n = int(token)
            return  True
        except Exception :
            return  False
    def cal(self,token,a,b):
        if token == "+":
            return a + b
        elif token == "-":
            return a - b
        elif token == "*" :
            return a * b
        elif token == "/":
            if a * b < 0 :
                return -((-a)/b)
            else:
                return a / b
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if len(tokens) == 0 :
            return 0
        stack = []
        for token in tokens:
            if self.isNum(token) :
                stack.append(int(token))
                continue
            else:
                v1 = stack[-1]
                v2 = stack[-2]
                del stack[-1]
                del stack[-1]
                v = self.cal(token,v2,v1)
                stack.append(v)
                print(stack)
        return stack[0]


