# coding=utf-8
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = []
        curlen, maxlen = 0, 0
        for curdir in input.split('\n'):
            depth = curdir.count('\t') # 当前目录或文件的深度
            while len(stack) > depth: # 计算当前目录或文件的绝对路径 长度
                curlen -= stack.pop()
            stack.append(len(curdir.strip ('\t')) + 1)
            curlen += stack[-1]
            if '.' in curdir:
                maxlen = max(maxlen, curlen - 1)
        return maxlen
