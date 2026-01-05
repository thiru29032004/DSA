class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor=0
    
        n=len(t)
        for i in range(n-1):
            xor^=ord(s[i])
            xor^=ord(t[i])
            
        xor^=ord(t[-1])
        return chr(xor)


        