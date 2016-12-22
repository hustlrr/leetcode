# coding=utf-8
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx1, idx2 = 0, len(numbers) - 1
        res = []
        while idx1 <= idx2:
            tmp = numbers[idx1] + numbers[idx2]
            if tmp == target:
                res.append(idx1 + 1)
                res.append(idx2 + 1)
                break
            elif tmp < target:
                idx1 += 1
            elif tmp > target:
                idx2 -= 1
        return res
