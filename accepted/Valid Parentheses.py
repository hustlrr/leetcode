# coding=utf-8
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=['' for i in range(len(s))]
        top=0
        for c in s:
            if top!=0 and ((c=='}' and stack[top-1]=='{') or \
            (c==']' and stack[top-1]=='[') or (c==')' and stack[top-1] =='(')):
                top-=1
            else:
                stack[top]=c
                top+=1
        return top==0
