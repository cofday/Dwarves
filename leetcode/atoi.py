__author__ = 'linweizhong'
"""
String to Integer (atoi)
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

--------
some check tip :
input : more then 2147483647 | output: 2147483647
input : "   +0 123" | output: 0
input : "  -0012a42" | output:0
input : "     +004500" | output:4500
input : "    010" | output:10
input : "+-2" | output: 0
input : "" | output:0
"""
class Solution:

    def convert(self,c):
        if c >= "0" and c <="9" : return 0,int(c)
        if c == "+" or c=="-" : return 1,c
        if c == " ":return 2,c
        return  3,c

    # @return an integer
    def atoi(self, str):
        str = str.strip()
        ilen = len(str)
        if ilen == 0 : return 0
        mark = ""
        sum = 0
        isNum,value = self.convert(str[0])
        if isNum == 1 :
            mark = str[0]
            str = str[1:]
        for index in range(len(str)):
            isNum,value = self.convert(str[index])
            if isNum != 0 : break
            sum = sum * 10 + value

        if mark == "-" :
            sum = sum * -1
            if sum < -2147483648:sum = -2147483648
        else:
            if sum > 2147483647 : sum = 2147483647
        return sum
