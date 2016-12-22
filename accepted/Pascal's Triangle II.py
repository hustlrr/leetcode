# coding=utf-8
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret=[1]
        for i in range(rowIndex):
            ret=[1]+[x+y for x,y in zip(ret[ :-1],ret[1:])]+[1]
        return ret

