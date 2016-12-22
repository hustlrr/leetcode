# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret=ListNode(0)
        ret.next=head
        p=ret
        while p.next and p.next.next:
            tmp=p.next.next
            p.next.next=tmp.next
            tmp.next=p.next
            p.next=tmp
            p=p.next.next
        return ret.next
