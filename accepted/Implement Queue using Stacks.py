# coding=utf-8
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=[]
        self.size=0


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)
        self.size+=1

    def pop(self):
        """
        :rtype: nothing
        """
        self.data.pop(0)
        self.size-=1


    def peek(self):
        """
        :rtype: int
        """
        return self.data[0]

    def empty(self):
        """
        :rtype: bool
        """
        return self.size==0
