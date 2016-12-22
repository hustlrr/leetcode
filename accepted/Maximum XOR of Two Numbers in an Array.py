# coding=utf-8
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask, maxnum = 0, 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixset = set()
            for num in nums:
                prefixset.add(num&mask)
            tmp = maxnum | (1 << i)
            #                 这里最初的想法是，两层循环遍 历prefixset看是否存在异或等 于tmp的组合
            # 如果prefix1 ^ prefix2 = tmp ,那么prefix1 ^ tmp = prefix
            for prefix in prefixset:
                if prefix ^ tmp in prefixset :
                    maxnum = tmp
                    break
        return maxnum
