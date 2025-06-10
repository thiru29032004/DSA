# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p1=l1
        p2=l2
        dn=ListNode(-1)
        temp=dn
        carry=0
        while p1 or p2:
            Sum=carry
            if p1:
                Sum+=p1.val
            if p2:
                Sum+=p2.val
            newNode=ListNode(Sum%10)
            carry=Sum//10
            temp.next=newNode
            temp=newNode
            if p1:
                p1=p1.next
            if p2:
                p2=p2.next
        if carry:
            temp.next=ListNode(carry)
        return dn.next

        
        