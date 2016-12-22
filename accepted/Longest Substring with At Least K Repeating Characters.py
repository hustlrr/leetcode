# coding=utf-8
import re
from collections import Counter


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = Counter(s)
        dispose_letter = [letter for letter, num in cnt.items() if num < k]
        if not dispose_letter:
            return len(s)
        subs = re.split('|'.join (dispose_letter), s)
        return max(self.longestSubstring(sub , k) for sub in subs)
