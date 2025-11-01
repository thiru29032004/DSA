# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,l1,l2):
        p1=l1
        p2=l2
        dn=ListNode(-1)
        lastNode=dn
        while p1 and p2:
            if p1.val<=p2.val:
                lastNode.next=p1
                lastNode=p1
                p1=p1.next
            else:
                lastNode.next=p2
                lastNode=p2
                p2=p2.next
        if p1:
            lastNode.next=p1
        if p2:
            lastNode.next=p2
        return dn.next

                

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return 
        ll=lists[0]
        for i in range(1,len(lists)):
            ll=self.merge(ll,lists[i])
        return ll


        