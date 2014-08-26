__author__ = 'linweizhong'
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0 :
            return 0
        ilen = len(A)-1
        newCount = 1
        p = 0
        q = 1
        while q <= ilen :
            if A[p] == A[q]:break
            p = p + 1
            q = q + 1
            newCount = newCount +1
        if q > ilen :
            return len(A)
        q = q + 1
        while q <= ilen :
            A[p+1]=A[q]
            if A[p] == A[p+1]:
                q = q +1
                continue
            else:
                p = p +1
                q = q +1
                newCount = newCount +1
        A = A[0:newCount]
        return newCount



