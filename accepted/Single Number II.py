# coding=utf-8
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnts=[0 for i in range(32)]
        for num in nums:
            for i in xrange(32):
                cnts[i]+=1 if(num&(1<<i)) else 0
        cnts=[cnt%3 for cnt in cnts]
        ans=sum([1<<i if cnt else 0 for i ,cnt in enumerate(cnts)])
        return ans if cnts[-1]==0 else ans -(1<<32)
