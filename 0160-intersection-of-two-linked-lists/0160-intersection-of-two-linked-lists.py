# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        st=set()
        temp1=headA
        while temp1:
            st.add(temp1)
            temp1=temp1.next
        temp2=headB
        while temp2:
            if temp2 in st:
                return temp2
            temp2=temp2.next
        return None
        