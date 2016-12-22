# coding=utf-8
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        if divisor == 0:
            return MAX_INT
        flag = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        tmp, add = divisor, 1
        while dividend >= divisor:
            if dividend >= tmp:
                res += add
                dividend -= tmp
            if dividend > (tmp << 1):
                tmp <<= 1
                add <<= 1
            elif dividend < tmp:
                tmp >>= 1
                add >>= 1
        return -res if flag else (MAX_INT 
