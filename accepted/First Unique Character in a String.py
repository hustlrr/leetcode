# coding=utf-8
from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charCnt = Counter(s)
        for idx, ch in enumerate(s):
            if charCnt.get(ch) == 1:
                return idx
        return -1
