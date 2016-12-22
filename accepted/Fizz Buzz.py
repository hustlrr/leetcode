# coding=utf-8
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        cnt3, cnt5 = 1, 1
        ret = []
        for i in range(n):
            tmp = ''
            if cnt3 % 3 == 0:
                tmp += 'Fizz'
            if cnt5 % 5 == 0:
                tmp += 'Buzz'
            if cnt3 % 3 and cnt5 % 5:
                tmp = str(i + 1)
            cnt3, cnt5 = cnt3 + 1, cnt5 + 1
            ret.append(tmp)
        return ret
