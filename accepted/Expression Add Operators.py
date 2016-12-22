# coding=utf-8
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        len_ = len(num)

        def dfs(exp, curidx, expvalue, prenum): #prenum 是前一个数的值(包含符号)
            if curidx == len_:
                if expvalue == target:
                    res.append(exp)
                return
            for i in range(curidx, len_):
                if num[curidx] == '0' and i - curidx >= 1:
                    return
                if curidx == 0:
                    dfs(num[curidx:i + 1], i + 1, int(num[curidx :i + 1]), int (num[curidx:i + 1]))
                else:
                    dfs(exp + '*' + num[curidx:i + 1], i + 1, expvalue - prenum + prenum * int (num[curidx:i + 1]),
                        int(num[curidx:i + 1]) * prenum)
                    dfs(exp + '+' + num[curidx:i + 1], i + 1, expvalue + int (num[curidx:i + 1]), int(num[curidx:i + 1] ))
                    dfs(exp + '-' + num[curidx:i + 1], i + 1, expvalue - int (num[curidx:i + 1]), -int(num[curidx:i + 1]))

        dfs('', 0, 0, 0)

