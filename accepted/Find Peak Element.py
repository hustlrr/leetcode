# coding=utf-8
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 如果大于两边返回当前index就可以 了，如果左边的节点比mid大，那 么我们可以继续在左半区间查找， 这里面一定存在一个peak，为什么 这么说呢？假设此时的区间范围为 [0, mid - 1]， 因为num[mid - 1]一定大于num[mid]了，如果num[ mid - 2] <= num[mid - 1]，那么num[mid - 1]就是一个peak。如果num[mid - 2] > num[mid - 1]，那么我们就继续在[0, mid - 2]区间查找，因为num[ -1]为负无穷，所以最终我们绝对 能在左半区间找到一个peak。同理 右半区间一样。
        #参考:https://siddontang.gitbooks .io/leetcode-solution/content /array/find_peak_element.html
        size = len(nums)
        low, high = 0, size-1
        while low < high:
            mid = low+(high-low)/2
            if mid+1 < size and nums[mid] > nums[mid+1]:
                high = mid # 说明峰值在左边
            else: # 说明峰值在右边

