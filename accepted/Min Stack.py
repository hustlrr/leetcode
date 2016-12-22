# coding=utf-8
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.minstack)==0 or self .minstack[-1]>=x:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        t=self.stack[-1]
        self.stack.pop()
        if t==self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
