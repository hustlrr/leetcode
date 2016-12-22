# coding=utf-8
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ''
        # 确定符号
        flag = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs (numerator), abs(denominator)
        # 先计算整数部分
        res += str(numerator / denominator)
        r = numerator % denominator
        if r == 0:
            return '-' + res if flag and res != '0' else res
        res += '.'
        # 计算小数部分
        remain_idx = {}
        while r:
            if remain_idx.has_key(r):
                idx = remain_idx[r]
                res = res[:idx] + '(' + res[idx:] + ')'
                break
            remain_idx[r] = len(res)
            r *= 10
            tmp = r / denominator
            r = r % denominator
            res += str(tmp)
        return '-' + res if flag and res != '0' else res
