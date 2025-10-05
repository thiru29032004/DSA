class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        Sum=0
        for i in range(len(nums)):
            if(i%2==0):
                Sum+=nums[i]
            else:
                Sum-=nums[i]
        return Sum
        