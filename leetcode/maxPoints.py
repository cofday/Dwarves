__author__ = 'linweizhong'

from node import  *


class Solution:

    def getSlope(self,p1,p2):
        x1 = p1.x
        y1 = p1.y
        x2 = p2.x
        y2 = p2.y
        if x1 != x2  :
            if y1 == y2 :
                a = "0.0"
            else :
                a = str(float(y1-y2)/float(x1-x2))
        else :
            a = "y"
        return a


    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) == 0 :
            return 0
        if len(points) == 1 :
            return  1
        plen = len(points)
        maxNum = 0
        lines={}
        for i in range(plen):
            lines.clear()
            samenum = 0
            for j in range(i+1,plen):
                if points[i].x == points[j].x and points[i].y == points[j].y :
                    samenum = samenum +1
                    continue
                key  = self.getSlope(points[i],points[j])
                if lines.has_key(key):
                    lines[key] = lines[key] +1
                else:
                    lines[key] = 1
            if samenum > maxNum:
                maxNum = samenum
            for k in lines :
                v = lines[k] +samenum
                if v > maxNum :maxNum = v
        return maxNum + 1




