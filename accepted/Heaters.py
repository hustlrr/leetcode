# coding=utf-8
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) # 对heater按照位置进行排序
        radius = 0
        for house in houses:
            low, high = 0, len(heaters) - 1
            while low <= high: # 二分查找，确定如果要插入heat ers，house的位置
                mid = low + (high - low) / 2
                if house > heaters[mid]:
                    low = mid + 1
                elif house < heaters[mid]:
                    high = mid - 1
                else:
                    low = mid
                    break
            # print('low=', low)
            if low == 0:
                radius = max(radius, heaters[low] - house)
            elif low == len(heaters):
                radius = max(radius, house - heaters[-1])
            else:
                radius = max(radius, min (heaters[low] - house, house - heaters[low - 1] ))
        return radius

