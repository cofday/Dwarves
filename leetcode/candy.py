__author__ = 'linweizhong'
"""
Candy
    There are N children standing in a line. Each child is assigned a rating value.
    You are giving candies to these children subjected to the following requirements:
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?
"""
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        ilen=len(ratings)-1
        count=[1 for x in ratings]
        for idx in range(ilen,0,-1):
            if ratings[idx] < ratings[idx-1]:
                count[idx-1] = count[idx]  + 1
        for idx in range(ilen):
            if ratings[idx] < ratings[idx +1] and count[idx] >= count[idx +1] :
                count[idx +1]= 1 + count[idx]

        return  sum(count)


