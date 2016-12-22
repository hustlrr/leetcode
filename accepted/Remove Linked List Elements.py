# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        myhead=ListNode(0)
        myhead.next=head
        pre,cur=myhead,head
        while cur:
            if cur.val==val:
                pre.next=pre.next.next
            else:
                pre=cur
            cur=cur.next
        return myhead.next
