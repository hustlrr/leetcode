# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        assitant=ListNode(0)
        assitant.next=head
        while head and head.next:
            tmp=head.next
            head.next=head.next.next
            tmp.next=assitant.next
            assitant.next=tmp
        return assitant.next
