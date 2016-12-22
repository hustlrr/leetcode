# coding=utf-8
class Solution(object):
    def comput(self,x,y,op):
        if op=='+':
            return x+y
        elif op=='-':
            return x-y
        else:
            return x*y

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        return [
            self.comput(x,y,op) for idx,op in enumerate(input) if op in '+-*'\
            for x in self.diffWaysToCompute (input[:idx])\
            for y in self.diffWaysToCompute (input[idx+1:])
        ]
