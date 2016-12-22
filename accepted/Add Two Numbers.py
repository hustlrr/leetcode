# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
        
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        nHead, flag = ListNode(0), 0
        head = nHead
        while flag or l1 or l2:
            node = ListNode(flag)
            if l1: 
                node.val += l1.val
                l1 = l1.next
            if l2: 
                node.val += l2.val
                l2 = l2.next
            flag = node.val // 10
            node.val %= 10
            head.next, head = node, node
        return nHead.next
