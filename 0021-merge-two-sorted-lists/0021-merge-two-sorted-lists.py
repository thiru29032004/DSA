# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dn=ListNode(-1)
        temp=dn
        p1=list1
        p2=list2
        while p1 and p2:
            if p1.val <p2.val:
                temp.next=p1
                temp=p1
                p1=p1.next
            else:
                temp.next=p2
                temp=p2
                p2=p2.next
        if p1:
            temp.next=p1
        if p2:
            temp.next=p2
        return dn.next
            
        