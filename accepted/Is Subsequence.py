# coding=utf-8
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idxs, idxt = 0, 0
        lens, lent = len(s), len(t)
        while idxs < lens and idxt < lent:
            if s[idxs] == t[idxt]:
                idxs += 1
                idxt += 1
            else:
                idxt += 1
        return idxs == lens
