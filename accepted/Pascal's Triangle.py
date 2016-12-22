# coding=utf-8
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret=[]
        if numRows == 0:
            return ret
        ret=[[1]]
        for row in range(1,numRows):
            tmp=[1]
            tmp.extend([x+y for x,y in zip (ret[-1][:-1],ret[-1][1:])])
            tmp.append(1)
            ret.append(tmp)
        return ret
