# coding=utf-8
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftcnt,rightcnt=0,0
        leftidx,rightidx=0,len(s)-1
        s=s.lower()
        while leftidx<rightidx:
            while not s[leftidx].isalnum() and leftidx<rightidx:
                leftidx+=1
            while not s[rightidx].isalnum() and leftidx<rightidx:
                rightidx-=1
            if leftidx<rightidx:
                if s[leftidx]!=s[rightidx]:
                    return False
                if s[leftidx].isalnum():
                    leftcnt+=1
                if s[rightidx].isalnum():
                    rightcnt+=1
            leftidx+=1
            rightidx-=1
        return leftcnt==rightcnt
