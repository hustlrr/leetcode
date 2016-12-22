# coding=utf-8
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head, step = 1, 1
        remaining = n
        left2right = True # 从左向右移动是True，否则是False
        while remaining > 1:
            #                 从左向右移动时，或者从右向左 移除之前剩余奇数个元素时，开 头元素会被移开
            if left2right or remaining % 2: 
                head += step
            remaining /= 2
            step *= 2
            left2right = (not left2right)
        return head
