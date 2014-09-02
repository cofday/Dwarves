__author__ = 'linweizhong'
"""
Spiral Matrix II
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0 :return []
        matrix = []
        for i in range(n):
            tmp=[0 for x in range(n)]
            matrix.append(tmp)
        num = 1
        i = 0
        j = n - 1
        while i <= j :
            for k in range(i,j+1):
                matrix[i][k] = num
                num = num +1
            for k in range(i+1,j+1):
                matrix[k][j] = num
                num = num +1
            for k in range(j-1,i-1,-1):
                matrix[j][k] = num
                num = num + 1
            for k in range(j-1,i,-1):
                matrix[k][i] = num
                num = num +1
            i = i + 1
            j = j -1
        return matrix


