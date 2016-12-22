# coding=utf-8
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 不能直接用split，这样空间复杂度太 高
        num_space = 0
        s = s.strip()
        s_len = len(s)
        i = 0
        while i < s_len:
            if s[i] == ' ' and ((i + 1 < s_len and s[i + 1] != ' ') or i + 1 == s_len):
                num_space += 1
            i += 1
        return num_space + 1 if s_len else 0
