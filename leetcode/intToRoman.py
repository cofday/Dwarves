__author__ = 'linweizhong'
"""
Integer to Roman
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    # @return a string
    def intToRoman(self, num):
        numbers=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanValues =["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        istr = ""
        while num > 0 :
            index = 0
            for valueindex in range(len(numbers)):
                if numbers[valueindex] <= num :
                    index = valueindex
                    break
            istr = istr + romanValues[index]
            num = num - numbers[index]
        print istr


