# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def revll(self,head):
        prev=None
        temp=head
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
    def findmiddle(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def isPalindrome(self, head):
        middle=self.findmiddle(head)
        temp1=head
        temp2=self.revll(middle)
        while temp1 and temp2:
            if temp1.val!=temp2.val:
                return False
            temp2=temp2.next
            temp1=temp1.next
        return True


        
        