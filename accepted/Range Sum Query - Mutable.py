# coding=utf-8
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.size = len(nums)
        self.nums = [0] * (self.size + 1)
        self.bitTree = [0] * (self.size + 1)
        for idx, num in enumerate(nums):
            self.update(idx, num)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        j = i + 1
        while j <= self.size:
            self.bitTree[j] += (val - self .nums[i + 1])
            j += (j & (-j))
        self.nums[i + 1] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j + 1) - self .getSum(i)

    def getSum(self, i): #计算前(i - 1 )个数字的和
        res = 0
        j = i
        while j > 0:
            res += self.bitTree[j]
            j -= (j & (-j))
        return res


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
