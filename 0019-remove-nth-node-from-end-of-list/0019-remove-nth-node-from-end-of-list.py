# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast=head
        for i in range(n):
            fast=fast.next
        if fast is None:
            return head.next
        slow=head
        while fast.next!=None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head
            

        
        