__author__ = 'linweizhong'
"""
Search in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) == 0  : return  -1
        tail = len(A) -1
        head = 0
        #|----------|--|
        #|--|----------|
        while tail >= head :
            mid = (tail + head) /2
            #print mid,tail,head
            if A[mid] == target : return  mid
            elif A[mid] > target :
                if A[mid] < A[head] :
                    tail = mid -1
                elif target >= A[head] :
                    tail = mid -1
                else:
                    head = mid + 1
            else:
                if A[tail] < A[mid] :
                    head = mid + 1
                elif   target <= A[tail] :
                    head = mid + 1
                else:
                    tail = mid - 1

        return  -1