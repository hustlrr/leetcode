# coding=utf-8
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[0]
        if n<1:
            return res
        res=[0,1]
        for i in range(1,n):
            for num in res[::-1]:
                res.append(num+(1<<i))
        return res
