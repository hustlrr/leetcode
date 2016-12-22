# coding=utf-8
import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.array = nums[:]
        self.original = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array[:] = self.original
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.array)
        return self.array


