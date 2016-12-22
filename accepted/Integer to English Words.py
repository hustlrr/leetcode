# coding=utf-8
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        words = ['', 'Thousand', 'Million', 'Billion']
        idx = 0
        res = []
        while num:
            tmp = self.transform3digits(num % 1000)
            if idx and tmp:
                tmp.append(words[idx])
            if tmp:
                res.append(tmp)
            num /= 1000
            idx += 1
        return ' '.join([' '.join(_) for _ in res[::-1]]).strip() if res else 'Zero'

    def transform3digits(self, num):
        words = [
            ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
             "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"],
            ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ]
        res = []
        digits = [num % 10, (num / 10) % 10, num / 100]
        if digits[2]:
            res.append(words[0][digits[2]])
            res.append('Hundred')
        if digits[1] >= 2:
            res.append(words[1][digits[1]])
            if words[0][digits[0]]:
                res.append (words[0][digits[0]])
        elif num % 100:
            res.append(words[0][num % 100])
        return res
