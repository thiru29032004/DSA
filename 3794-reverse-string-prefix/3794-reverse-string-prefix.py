class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        res=""
        n=len(s)
        for i in range(k):
            res=s[i]+res
        for i in range(k,n):
            res+=s[i]
        return res
        