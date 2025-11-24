class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            c=0
            for j in range(n):
                if i!=j and nums[i]>nums[j]:
                    c+=1
            ans[i]=c
        return ans

                    





        