# coding=utf-8
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res=[[0 for i in range(n)] for j in range(n)]
        directs=[(0,1),(1,0),(0,-1),(-1,0)]
        x,y=0,0
        cnt=1
        for i in range(n/2):
            x,y=i,i
            for direct in directs:
                for j in range(n-1-2*i):
                    res[x][y]=cnt
                    cnt+=1
                    x+=direct[0]
                    y+=direct[1]
        if n%2:
            res[n/2][n/2]=cnt
        return res
