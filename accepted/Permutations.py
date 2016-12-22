# coding=utf-8
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size=len(nums)
        res=[sorted(nums)]
        for i in range(size-1):
            tmp=[]
            for n in res:
                for j in range(i,size):
                    next=[num for num in n]
                    next[i],next[j]=next[j] ,next[i]
                    tmp.append(next)
            res=tmp
        return res
