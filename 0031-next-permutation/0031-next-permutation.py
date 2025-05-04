class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break
        if index==-1:
            return nums.reverse()
        for i in range(n-1,-1,-1):
            if nums[index]<nums[i]:
                nums[index],nums[i]=nums[i],nums[index]
                break
        left=index+1
        right=n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
        