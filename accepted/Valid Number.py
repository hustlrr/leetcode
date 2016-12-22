# coding=utf-8
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        s = s.strip()
        len_ = len(s)
        if len_ == 0:
            return False
        dogFlag, eFlag = False, False
        for idx, letter in enumerate(s):
            if letter == '.':
                if eFlag or dogFlag or \
                        ((idx == 0 or not '0' <= s[idx - 1] <= '9') and \
                                 (idx + 1 == len_ or not '0' <= s[idx + 1] <= '9')):
                    return False
                dogFlag = True
            elif letter == 'e' or letter == 'E':
                if idx == 0 or idx + 1 == len_ or eFlag:
                    return False
                eFlag = True
            elif letter == '+' or letter == '-':
                if (idx > 0 and s[idx - 1] ! = 'e' and s[idx - 1] != 'E') or \
                                        idx + 1 == len_ or \
                        not ('0' <= s[idx + 1] <= '9' or s[idx + 1] == '.'):
                    return False
            elif '0' <= letter <= '9':
                continue
            else:
                return False
        return True

