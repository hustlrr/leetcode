# coding=utf-8
from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letterCnt = Counter(s)
        visited = set()
        stack = []
        for letter in s:
            letterCnt[letter] -= 1
            if letter in visited:
                continue
            while stack and stack[-1] > letter and letterCnt[stack[ -1]] > 0:
                visited.remove(stack[-1])
                stack.pop()
            visited.add(letter)
            stack.append(letter)
        return ''.join(stack)
