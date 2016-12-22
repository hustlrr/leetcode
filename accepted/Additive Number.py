# coding=utf-8
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def add(x, y, s):
            if len(s) == 0:
                return True
            tmp = str(int(x) + int(y))
            if (x[0] == '0' and len(x) != 1) or (y[0] == '0' and len(y) ! = 1) or s[0] == '0':
                return False
            if s.startswith(tmp):
                return add(y, tmp, s[len(tmp ):])
            else:
                return False

        size = len(num)
        flag = False
        for i in range(1, size / 2 + 1):
            for j in range(1, size / 2 + 1):
                if i + j >= size:
                    break
                if (num[0] == '0' and i != 1 ) or (num[i] == '0' and j != 1) or num[i + j] == '0':
                    continue
                if num[i + j:].startswith (str(int(num[:i]) + int (num[i:i + j]))):
                    flag = flag or add(num[ :i], num[i:i + j], num[i + j:])
                if flag:
                    return flag
        return flag
