class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        psm={}
        n=len(nums)
        MinLen=float('inf')
        flag=False
        Sum=0
        for i in range(n):
            Sum+=nums[i]
            if Sum==target:
                flag=True
                MinLen=min(MinLen,i+1)
            rem=Sum-target
            if rem in psm:
                flag=True
                MinLen=min(MinLen,i-psm[rem])
            psm[Sum]=i
        if flag:
            return MinLen
        else:
            return 0
            
        