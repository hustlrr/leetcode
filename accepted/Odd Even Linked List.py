# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1,head2=head,ListNode(0)
        head2.next=None
        p2=head2
        while p1 and p1.next:
            tmp=p1.next
            p1.next=p1.next.next
            tmp.next=p2.next
            p2.next=tmp
            p1=p1.next
            p2=p2.next
        p1=head
        while p1 and p1.next:
            p1=p1.next
        if p1:
            p1.next=head2.next
        return head
