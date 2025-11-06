class Solution:
    def rotate(self,s,k):
        res=s[k:]+s[:k]


    def rotateString(self, s: str, goal: str) -> bool:

        
        k=0
        while k!= len(s):
            if s[k:]+s[:k] == goal:
                return True
            k+=1
        return False

        


        