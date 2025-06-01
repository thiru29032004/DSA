class Solution(object):
    def maxProduct(self, nums):

        maxprt=float('-inf')
        n=len(nums)
        pre=1
        suff=1
        for i in range(n):
          
            pre*=nums[i]
            suff*=nums[(n-1)-i]
            maxprt=max(maxprt,(max(pre,suff)))
            if pre==0:
                pre=1
            if suff==0:
                suff=1
        return maxprt


        