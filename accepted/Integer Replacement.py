# coding=utf-8
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def myDivide(num, res):
            if num == 0:
                return 0
            elif num == 1:
                return res
            elif num % 2 == 0:
                return myDivide(num >> 1, res + 1)
            else:
                return min(myDivide(num + 1, res + 1), myDivide(num - 1, res + 1))
        return myDivide(n, 0)
