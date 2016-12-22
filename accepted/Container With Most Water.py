# coding=utf-8
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        res=0
        while left<right:
            area=min(height[left] ,height[right])*(right-left)
            if height[left]<height[right]: #短板在左边，左边前移
                left+=1
            else:
                right-=1
            res=max(res,area)
        return res
