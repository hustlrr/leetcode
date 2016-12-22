# coding=utf-8
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # 尽量移除靠左的且值更大的k个元素
        len_prev = len(num)
        len_removed = len_prev - k
        remainings = []
        for digit in num:
            while k > 0 and len(remainings) and digit < remainings[-1]:
                remainings.pop()
                k -= 1
            remainings.append(digit)
        start_idx = 0 # 确定第1个非0元素在栈中的位置
        while start_idx < len_removed and remainings[start_idx] == '0':
            start_idx += 1
        return '0' if start_idx == (len_removed) else ''.join (remainings[start_idx:start_idx + len_removed])

