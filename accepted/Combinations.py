# coding=utf-8
class Solution(object):
    def dfs(self,res,path,n,k,value):
        '''
        value:当前层的值
        '''
        if k==0:
            res.append(path[:])
            return
            # print path
        if value>n:
            return
        self.dfs(res,path,n,k,value+1)
        path.append(value)
        self.dfs(res,path,n,k-1,value+1)
        path.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        path=[]
        self.dfs(res,path,n,k,1)
        return res
