# coding=utf-8
# Below is the interface for Iterator, which is already defined for you.
#
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter=iterator
        self.peekFlag=False
        self.nextElem=None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peekFlag:
            self.peekFlag=True
            self.nextElem=self.iter.next()
        return self.nextElem

    def next(self):
        """
        :rtype: int
        """
        if not self.peekFlag:
            self.nextElem=self.iter.next()
        self.peekFlag=False
        return self.nextElem

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peekFlag or self.iter .hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek() # Get the next element but not advance the iterator.
#     iter.next() # Should return the same value as [val].
