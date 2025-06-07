# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        arr=[]
        p1=list1
        p2=list2
        while p1 and p2:
            if p1.val<p2.val:
                arr.append(p1.val)
                p1=p1.next
            else:
                arr.append(p2.val)
                p2=p2.next
        while p1:
            arr.append(p1.val)
            p1=p1.next
        while p2:
            arr.append(p2.val)
            p2=p2.next
        dn=ListNode(-1)
        temp=dn
        for num in arr:
            temp.next=ListNode(num)
            temp=temp.next
        return dn.next

            


        