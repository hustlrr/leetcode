# coding=utf-8
class Solution(object):
    def __init__(self):
        self.hours = {0:['0']}
        self.minutes = {0:['00']}
        from itertools import combinations
        for num_bits in range(1, 4): # 小时的位置最多有3个led灯亮
            hour = []
            for bits in combinations(range(4 ), num_bits):
                s = sum([1 << bit for bit in bits])
                if s > 11: # 小时最多为11
                    continue
                hour.append(str(s))
            self.hours[num_bits] = hour
        for num_bits in range(1, 6): # 分钟的位置最多有5个led灯亮
            minute = []
            for bits in combinations(range(6 ), num_bits):
                s = sum([1 << bit for bit in bits])
                if s > 59: # 分钟最多为59
                    continue
                minute.append('%02d' % s)
            self.minutes[num_bits] = minute

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        mask = '%s:%s'
        res = []
        for num_hour in range(num + 1):
            num_min = num - num_hour
            try:
                for h in self .hours[num_hour]:
                    for m in self .minutes[num_min]:
                        res.append(mask % (h , m))
            except KeyError:
                pass
        return res
