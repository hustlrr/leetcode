# coding=utf-8
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        idx1, idx2 = 0, 0
        num1, num2 = num1[::-1], num2[ ::-1]
        carry = 0
        sum = ''
        while idx1 < len1 and idx2 < len2:
            sum += str((int(num1[idx1]) + int(num2[idx2]) + carry) % 10)
            carry = (int(num1[idx1]) + int (num2[idx2]) + carry) / 10
            idx1, idx2 = idx1 + 1, idx2 + 1
        while idx1 < len1:
            sum += str((int(num1[idx1]) + carry) % 10)
            carry = (int(num1[idx1]) + carry) / 10
            idx1 += 1
        while idx2 < len2:
            sum += str((int(num2[idx2]) + carry) % 10)
            carry = (int(num2[idx2]) + carry) / 10
            idx2 += 1

