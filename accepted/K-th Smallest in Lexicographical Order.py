# coding=utf-8
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur = 1
        k = k - 1
        while k > 0:
            steps = self.calSteps(n, cur, cur+1)
            if k >= steps:
                cur = cur + 1
                k -= steps
            else:
                cur = cur * 10
                k -= 1
        return cur

    def calSteps(self, n, n1, n2):
        steps = 0
        while n1 <= n:
            steps += min(n + 1, n2) - n1
            n1 *= 10
            n2 *= 10
        return steps

