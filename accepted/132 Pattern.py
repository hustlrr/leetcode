# coding=utf-8
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        right = -(1 << 31)
        stack = []
        for num in nums[::-1]:
            if num < right: # 此时stack一定不空，所以一定有 s2>right (由出栈规则只栈中的元素一定大 于right)
                return True
            else:
                while len(stack) and num > stack[-1]: # 栈里存放 (s1,s2,s3)中的s2
                    right = stack.pop(-1) # right是s3 ,所以如果不存在(s2>s3 )的话，那么right一直为 “无穷小”
            stack.append(num)
        return False

