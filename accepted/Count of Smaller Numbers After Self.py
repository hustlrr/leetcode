# coding=utf-8
class Solution(object):
    def getPos(self, num, insertArray):
        start = 0
        end = len(insertArray) - 1
        while start <= end:
            mid = start + (end - start)/2
            if insertArray[mid] >= num:
                end = mid - 1
            elif insertArray[mid] < num:
                start = mid + 1
        insertArray.insert(start, num)
        return start
            
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        insertArray = []
        res = []
        for num in nums[::-1]:
            pos = self.getPos(num, insertArray)
            res.append(pos)
        return res[::-1]
