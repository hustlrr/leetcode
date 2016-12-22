# coding=utf-8
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start, end = 0, 0
        longest = 0
        letter_cnt = [0] * 26
        freq_cnt = 0
        while end < len(s):
            letter = ord(s[end]) - ord('A' )
            letter_cnt[letter] += 1
            if letter_cnt[letter] > freq_cnt:
                freq_cnt += 1

            if end - start + 1 - freq_cnt > k: # 窗口的最大长度应该是k + freq_cnt
                letter = ord(s[start]) - ord('A')
                letter_cnt[letter] -= 1
                #                     出现最频繁的字母可能会 发生变化，所以此处要更 新
                for i in range(26):
                    if letter_cnt[i] > freq_cnt:
                        freq_cnt = letter_cnt[i]
                start += 1

