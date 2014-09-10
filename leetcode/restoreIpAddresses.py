__author__ = 'linweizhong'
"""
Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution:
    def __init__(self):
        self.result = []

    def isValid(self,value):
        v = int(value)
        if v > 255 or v < 0  : return False
        newValue = str(v)
        if len(newValue) != len(value) : return  False
        return  True

    def buildIpAddress(self,s,idx,ipstr):
        if idx == 4 and len(s) == 0 :
            self.result.append(ipstr)
            return
        if idx == 4 :
            return
        if len(s) >= 1 :
            ip = s[0]
            if self.isValid(ip) :
                newipstr = "%s.%s"%(ipstr,ip)
                self.buildIpAddress(s[1:],idx +1 ,newipstr)

        if len(s) >= 2 :
            ip = s[:2]
            if self.isValid(ip) :
                newipstr = "%s.%s"%(ipstr,ip)
                self.buildIpAddress(s[2:],idx+1 ,newipstr)

        if len(s) >= 3 :
            ip = s[:3]
            if self.isValid(ip) :
                newipstr = "%s.%s"%(ipstr,ip)
                self.buildIpAddress(s[3:],idx +1 ,newipstr)


    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if len(s)==0 :
            return  []
        ipstr = ""
        self.buildIpAddress(s,0,ipstr)
        self.result =[ x[1:] for x in self.result ]
        return  self.result

