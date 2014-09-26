__author__ = 'linweizhong'
"""
Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution:
    def __init__(self):
        self.numMap={
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"],
        }
    def buildCombinations(self,digits):
        if len(digits) == 0 : return None
        combinations = self.buildCombinations(digits[1:])
        index = int(digits[0])
        if index < 2 or index  > 9 :
            return combinations
        array = self.numMap[index]
        if combinations == None : return  array
        newcombinations = []
        for item in combinations :
            for prefix in array :
                istr = "%s%s"%(prefix,item)
                newcombinations.append(istr)
        if len(newcombinations) == 0 : return array
        return newcombinations

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if len(digits)== 0 : return [""]
        return  self.buildCombinations(digits)
