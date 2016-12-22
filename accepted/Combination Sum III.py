# coding=utf-8
class Solution(object):
    def dfs(self,res,path,value,k,target):
        """
        :type res:list
        :type path:list
        path:当前路径
        res:结果集合
        value:当前层的值
        """
        s=sum(path)
        if s==target and k==0:
            res.append(path[:])
            # print path
            return
        elif s>target or k==0 or value >=min(9,target):
            return
        self.dfs(res,path,value+1,k,target )
        path.append(value+1)
        self.dfs(res,path,value+1,k-1 ,target)
        path.pop()

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        path=[]

