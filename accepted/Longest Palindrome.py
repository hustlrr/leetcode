# coding=utf-8
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnts = 0
        from collections import Counter
        letterFreq = Counter(s)
        existOddFreq = False
        for freq in letterFreq.values():
            cnts += (freq - 1 if freq % 2 else freq)
            if freq % 2:
                existOddFreq = True
        cnts += (1 if existOddFreq else 0) # 特殊情况是，字符串长度为奇数时， 中间出现的字符的词频可以为奇数
        return cnts

