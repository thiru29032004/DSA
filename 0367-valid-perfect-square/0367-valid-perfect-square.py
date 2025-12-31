class Solution:
    def findSquareRoot(self,num):
        l,h,ans=1,num,0
        while l<h:
            mid=(l+h)//2
            if mid*mid==num:
                return mid
            elif mid*mid<num:
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans

    def isPerfectSquare(self, num: int) -> bool:
        val=self.findSquareRoot(num)
        if val*val==num:
            return True
        else:
            return False
        