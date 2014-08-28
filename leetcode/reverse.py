__author__ = 'linweizhong'
"""
#Reverse Integer
#   Reverse digits of an integer.
#       Example1: x = 123, return 321
#       Example2: x = -123, return -321
"""
class Solution:
    # @return an integer
    def reverse(self, x):
        import  sys
        istr = str(x)
        symbol = 0
        if istr[0] == "+" or istr[0] == "-":
            symbol = 1
        try:
            if symbol == 0  :
                return int(istr[::-1])
            else:
                newistr=istr[1:]
                newValue  = int(newistr[::-1])
                if istr[0] == "-":
                    newValue = newValue * -1
                return newValue
        except Exception :
            sys.exit(1)



