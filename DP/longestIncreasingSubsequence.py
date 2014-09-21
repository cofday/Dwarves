__author__ = 'linweizhong'
# coding:utf-8
"""
一个序列有N个数：A[1],A[2],…,A[N]，求出最长非降子序列的长度
"""

class Solution :

    def lis (self,A):
        """
        定义状态d(i),表示前i个数中，以A[i]结尾的最长非降子序的长度

        #example :
        #A = [5，3，4，8，6，7]
        前1个数的LIS长度 d(1) = 1 (序列 : 5)
        前2个数的LIS长度 d(2) = 1 (序列 : 3)
        前3个数的LIS长度 d(3) = 2 (序列 : 3,4 ;  d(3) = d(2) +1
        前4个数的LIS长度 d(4) = 3 (序列 : 3,4,8; d(4) = max{d(1),d(2),d(3)} +1 = 3 )
        所以状态方程:
            d(i) = {1,d(j) +1} ,其中i > j ,A[i] > A[j]
        本题的解法的时间复杂度是O(n^2)
        """

        ilen = len(A)
        d = [0 for x in xrange(ilen)]
        maxlen = 1
        for idx in xrange(ilen):
            d[idx] = 1
            for jdx in xrange(idx):
                if A[idx] > A[jdx] and d[jdx] + 1 > d[idx] :
                    d[idx] = d[jdx] + 1
            if maxlen  < d[idx] : maxlen = d[idx]

        return  maxlen

    def lis2(self,A):
        """
        O(nlogn)的算法
        维护一个数组B，存储LIS最小最小末尾，假设最小非降字串的长度是maxlen

        example :
        A = [5，3，4，8，6，7]
        将A(1)＝5有序的放到B中,B[0]＝5,也就是说当只有一个数字5的时候，长度为1的LIS的最小末尾是5，maxlen=1
        将A(2)＝3有序的放在B中,B[0]=3,也就是说长度为1的LIS的最小末尾是1,B[0]=5被替换
        将A(3)＝4,A[3] > B[0],所以令B[0+1] = A[3],也就是长度为2的LIS的最小末尾为4,maxlen = 2
        ......

        所以数组B中不是真正的LIS结果，只是存储了对应长度LIS的最小末尾
        在B中插入数据是有序的，而且是进行替换而不需要挪动——也就是说，我们可以使用二分查找，将每一个数字的插入时间优化到O(logN)
        于是算法的时间复杂度就降低到了O(NlogN)！
        """
        B=[0 for x in xrange(len(A))]
        B[0] = A[0]
        ilenB=1
        for idx in xrange(1,len(A)):
            left = 0
            right = ilenB
            while right >= left :
                mid = (right +left)/2
                if B[mid] < A[idx] :left = mid +1
                else :right = mid -1
            B[left] = A[idx]
            if left > ilenB :  ilenB = ilenB +1
        return  ilenB







