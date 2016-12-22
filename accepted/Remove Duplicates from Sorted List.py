# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pp=head
        np=None
        if head:
            np=head.next
        while np:
            while np and np.val==pp.val:
                np=np.next
            pp.next=np
            pp=np
        return head
