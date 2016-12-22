# coding=utf-8
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        maskleft,maskright=1,1
        while x/maskleft:
            maskleft*=10
        maskleft/=10
        while maskleft>maskright:
            if (x/maskleft)%10!=(x% (maskright*10))/maskright:
                return False
            maskleft/=10
            maskright*=10
        return True
