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
        return prev,head
    def findKthNode(self,head,k):
        c=0
        temp=head
        while temp:
            c+=1
            if c==k:
                break
            temp=temp.next
        return temp
    def reverseKGroup(self, head, k):
        temp=head
        dn=ListNode(-1)
        prevLast=dn
        while temp:
            kthNode=self.findKthNode(temp,k)
            if kthNode is None:
                prevLast.next=temp
                break
            nextNode=kthNode.next
            kthNode.next=None
            newNode,newTail=self.revll(temp)
            prevLast.next=newNode
            prevLast=newTail
            temp=nextNode
        return dn.next


        