# coding=utf-8
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        concate = s + '#' + s[::-1]
        p = [0 for _ in range(len(concate))] # 记录前后缀共同字串长度
        for j in range(1, len(concate)):
            i = p[j - 1]
            while i and concate[i] != concate[j]:
                i = p[i - 1]
            if concate[i] == concate[j]:
                p[j] = i + 1
        return s[::-1][:len(s)-p[-1]] + s

