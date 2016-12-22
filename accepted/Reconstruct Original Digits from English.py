# coding=utf-8
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        vocab = [(6, 'six'), (0, 'zero'), (2, 'two'), (8, 'eight'), (7, 'seven'),
                 (4, 'four'), (5, 'five'), (9, 'nine'), (1, 'one'), (3, 'three')]
        res = ''
        from collections import Counter
        letter_cnt = Counter(s) # 记录字符串中各个字母的出现次数
        digit_idx = 0
        while digit_idx < 10:
            num, word = vocab[digit_idx]
            existflag = True
            digit_letter_cnt = Counter (word) # 记录每个数字中的各个字母出 现的次数
            for letter, cnt in digit_letter_cnt.items():
                if letter_cnt[letter] - cnt < 0:
                    existflag = False
                    digit_idx += 1 # 一个数字可能出现多次， 所以要判断字符串中不 可能再有这个数字后才 转到下一个数字的判断
                    break
            if existflag:
                for letter, cnt in digit_letter_cnt.items ():
                    letter_cnt[letter] -= cnt
                res += str(num)

