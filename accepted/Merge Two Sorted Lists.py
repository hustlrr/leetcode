# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=p=ListNode(0)
        p1,p2=l1,l2
        while p1 and p2:
            if p1.val<p2.val:
                p.next=p1
                p1=p1.next
            else:
                p.next=p2
                p2=p2.next
            p=p.next
        p.next=(p1 if p1 else p2)
        return head.next
