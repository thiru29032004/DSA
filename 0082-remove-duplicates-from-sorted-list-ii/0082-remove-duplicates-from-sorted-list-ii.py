# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap={}
        temp=head
        while temp:
            hashMap[temp.val]=hashMap.get(temp.val,0)+1
            temp=temp.next
        
        dn=ListNode(-1)
        temp=head
        lastNode=dn
        while temp:
            if hashMap[temp.val]==1:
                lastNode.next=temp
                lastNode=temp
            temp=temp.next
        lastNode.next=None
        return dn.next

        