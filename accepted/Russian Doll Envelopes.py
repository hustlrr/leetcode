# coding=utf-8
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = sorted(envelopes, cmp =lambda ex, ey: ex[0] - ey[0] if ex[0] != ey[0] else ey[1] - ex[1])
        #问题转变为求信封高的最长子序列
        print envelopes
        dp = []
        if len(envelopes):
            dp.append(envelopes[0][1])
        for i in range(1,len(envelopes)):
            if envelopes[i][1] > dp[-1]:
                dp.append(envelopes[i][1])
            elif envelopes[i][1] < dp[0]:
                dp[0] = envelopes[i][1]
            else:
                low, high = 0, len(dp) - 1
                while low <= high:
                    mid = low + (high - low ) / 2
                    if envelopes[i][1] > dp[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                dp[low] = envelopes[i][1]
        return len(dp)
