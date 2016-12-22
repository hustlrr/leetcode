# coding=utf-8
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=int(''.join(map(str,digits)))+1
        ret=[]
        while num:
            ret.append(num%10)
            num/=10
        return ret[::-1]
