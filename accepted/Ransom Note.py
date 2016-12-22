# coding=utf-8
from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letterCnt = Counter(magazine)
        for letter in ransomNote:
            cnt = letterCnt[letter]
            if cnt:
                letterCnt[letter] = cnt - 1
            else:
                return False
        return True
