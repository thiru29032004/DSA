class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)-1
        while n>=0:
            last=int(num[n])
            if last%2!=0:
                res= "".join(num[:n+1])
                return res
            n-=1
        return ""

        