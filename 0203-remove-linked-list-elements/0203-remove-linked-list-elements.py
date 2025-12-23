# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dn=ListNode(-1)
        dn.next=head
        temp=dn
        prev=temp
        while temp:
            nxt=temp.next
            if temp.val==val:
                prev.next=nxt
            else:
                prev=temp
            temp=temp.next
        return dn.next

        