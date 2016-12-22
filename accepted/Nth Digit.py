# coding=utf-8
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_bits = 1
        num_nums = 9
        total_bits = 0
        while total_bits + num_nums * num_bits < n:
            total_bits += num_nums * num_bits
            num_nums *= 10
            num_bits += 1
        # 确定是位数为num_bits的数字中的第几 个数
        i = (n - 1 - total_bits) / num_bits # 第(i)个数
        j = (n - total_bits - num_bits * i) # 第j位
        return int(str(10 ** (num_bits - 1) + i)[j - 1])

