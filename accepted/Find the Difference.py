# coding=utf-8
from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnts = Counter(s)
        cntt = Counter(t)
        for ch, cnt in cntt.items():
            if cnts.get(ch, 0) != cnt:
                return ch
