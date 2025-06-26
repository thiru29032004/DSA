# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findlen(self,headA,headB):
        l1=0
        l2=0
        temp1=headA
        temp2=headB
        while temp1 or temp2:
            if temp1:
                l1+=1
                temp1=temp1.next
            if temp2:
                l2+=1
                temp2=temp2.next
        return l1-l2
    def getIntersectionNode(self, headA, headB):
        diff=self.findlen(headA,headB)
        temp2=headB
        temp1=headA
        if diff<0:
            
            while diff!=0:
                temp2=temp2.next
                diff+=1
        
        else:
            
            while diff!=0:
                temp1=temp1.next
                diff-=1
      
        while temp1 and temp2:
            if temp1==temp2:
                return temp1
            temp1=temp1.next
            temp2=temp2.next
        return None

        
        