# coding=utf-8
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[1,1,2]
        for i in range(3,n+1):
            tmp=0
            for j in range(1,i+1):
                tmp+=(res[j-1]*res[i-j])
            res.append(tmp)
        return res[n]
