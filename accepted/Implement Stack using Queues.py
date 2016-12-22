# coding=utf-8
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0
