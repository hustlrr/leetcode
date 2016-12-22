# coding=utf-8
class Solution(object):
    def repeatedSubstringPattern(self, str ):
        """
        :type str: str
        :rtype: bool
        """
        len_all_str = len(str)
        len_sub_str = 1
        while len_sub_str * 2 <= len_all_str:
            if len_all_str % len_sub_str ! = 0:
                len_sub_str += 1
                continue
            i = 1
            while i * len_sub_str <= len_all_str:
                if str[(i - 1) * len_sub_str:i * len_sub_str] != str[ :len_sub_str]:
                    break
                i += 1
            if i * len_sub_str > 
