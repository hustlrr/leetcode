# coding=utf-8
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        lens, lenp = len(s), len(p)
        res = []
        if lenp:
            cntp = Counter(p)
        else:
            return res
        start, end = 0, 0
        cnts = {}
        while end < lens:
            cnts[s[end]] = cnts.get(s[end], 0) + 1
            if end - start + 1 == lenp:
                flag = True
                for letter, cnt in cntp .items():
                    if cnts.get(letter, 0) ! = cnt:
                        flag = False
                        break
                if flag: # 当前s[start :end+1]是一个anagrams
                    res.append(start)
                cnts[s[start]] = cnts.get (s[start], 0) - 1
                start += 1
            end += 1
        return res
