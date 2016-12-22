# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findMiddle(self,head):
        '''
        找到中间节点
        '''
        myHead=ListNode(0)
        myHead.next=head
        fast,slow=myHead,myHead

        while fast and slow:
            fast=fast.next
            if fast==None:
                break
            fast=fast.next
            slow=slow.next
        return slow

    def myReverse(self,head):
        '''
        head是头结点
        '''
        if head==None:
            return head
        p=head.next
        while p and p.next:
            tmp=p.next
            p.next=tmp.next
            tmp.next=head.next
            head.next=tmp
        return head.next

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        middle=self.findMiddle(head)
        middle.next=self.myReverse(middle)
        p1,p2=head,middle.next if middle else None
        while p1 and p2:
            if p1.val!=p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True
