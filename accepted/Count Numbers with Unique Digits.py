# coding=utf-8
class Solution(object):
    num_of_eachdigit = [10,81]
    for i in range(3,11):
        num_of_eachdigit.append (num_of_eachdigit[-1]*(11-i))
        
    def countNumbersWithUniqueDigits(self, n ):
        """
        :type n: int
        :rtype: int
        """
        return sum(self.num_of_eachdigit[:n] ) if n != 0 else 1
