# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        d1=headA
        d2=headB
        while d1!=d2:
            if d1:
                d1=d1.next
            else:
                d1=headB
            if d2:
                d2=d2.next
            else:
                d2=headA
        return d1
        