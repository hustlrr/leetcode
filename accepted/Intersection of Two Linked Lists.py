# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lena,lenb=0,0
        pa,pb=headA,headB
        while pa:
            pa=pa.next
            lena+=1
        while pb:
            pb=pb.next
            lenb+=1
        pa,pb=(headA,headB) if lena>lenb else (headB,headA)
        for i in range(max(lena-lenb,lenb -lena)):
            pa=pa.next
        while pa and pb:
            if pa==pb:
                return pa
            pa=pa.next
            pb=pb.next
        return None
