# coding=utf-8
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        letter =[str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
        res = ''
        if num < 0:
            num = (1 << 32) + num
        while num:
            res += letter[num % 16]
            num /= 16
        return res[::-1] if len(res) else '0'
