__author__ = 'linweizhong'
# coding:utf-8
"""
Container With Most Water
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

本来想的是最土的n(n^2)
网上看了O(n)的解法。甚妙！
假设直线定义如下 :
 L1 ...(Lx)....L2  .... R2 ...(Rx)... R1
 Lx 都小于 L1
 Rx 都小于 R1
 L1 < L2
 R1 < R1

初始状态设置为L1,R1，这样的宽度最大;然后缩小宽度,那么宽度就要比原来的高,缩小的办法是,如果L1小于R1,那么L1往右移动,如果L1大于R1,则R1向左移动

证明:
    L1<R1<R2<L2,那么在L1移动到L2和R1移动到R2的过程中,存在的Lx和Rx都满足Lx < L1, Rx < R1;
    假设Lx < Rx,那么Lx* d(Rx - Lx) < L1*d(Rx-Lx) < L1 * ( R1 - L1);
    若Lx > Rx,则Rx * d(Rx - Lx) < Rx * d(R1 - L1) < L1 * d(R1 - L1) (因为Rx,Lx都小于L1<R1)
"""
class Solution:
    def min(self,a,b):
        if a > b : return b
        return a
    # @return an integer
    def maxArea(self, height):
        maxarea = (self.min(height[0],height[-1]) *(len(height)-1))
        startIdx = 0
        endIdx = len(height)-1
        while startIdx < endIdx :
            if height[startIdx] > height[endIdx] :
                endIdx = endIdx -1
            else :
                startIdx = startIdx +1
            h =self.min(height[startIdx],height[endIdx])
            area = (endIdx - startIdx) * h
            if area  > maxarea  :
                maxarea = area
        return maxarea