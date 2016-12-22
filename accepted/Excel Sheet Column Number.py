# coding=utf-8
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        v=1
        for c in s[::-1]:
            res+=(ord(c)-ord('A')+1)*v
            v*=26
        return res
