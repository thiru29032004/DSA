class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        Sorted=sorted(nums)
        ans=[]
        for i in range(len(nums)):
            ans.append(Sorted.index(nums[i]))
        return ans

        