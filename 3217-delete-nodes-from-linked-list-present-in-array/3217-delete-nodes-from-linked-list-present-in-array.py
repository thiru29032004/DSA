# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dn=ListNode(-1)
        lastNode=dn
        st=set()
        for num in nums:
            st.add(num)
        temp=head
        while temp:
            if temp.val not in st:
                lastNode.next=temp
                lastNode=temp
            temp=temp.next
        lastNode.next=None
        return dn.next

        