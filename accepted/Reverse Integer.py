# coding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=1 if x>=0 else -1
        x=x*flag
        res=0
        mask=1
        while not 1<=x/mask<10 and x:
            mask*=10
        while x:
            res+=(x%10)*mask
            x/=10
            mask/=10
        return res*flag if res<=(2<<30)-1 else 0
