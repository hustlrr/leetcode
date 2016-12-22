# coding=utf-8
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        def remove(str, start, end, parentheses):
            cnt = 0
            for idx, c in enumerate(str):
                if c == parentheses[0]:
                    cnt += 1
                elif c == parentheses[1]:
                    cnt -= 1
                if cnt >= 0: 
                    continue
                for idy in range(end, idx +1):
                    if str[idy] == parentheses[1] and (str[idy - 1] != parentheses[1] or idy == end):
                        remove(''.join (str[:idy]+str[idy+1 :]), idx, idy, parentheses)
                return
            str_reversed = str[::-1]
            if parentheses[0] == '(':
                remove(str_reversed, 0, 0, [')','('])
            else:
                ans.append(str_reversed)

