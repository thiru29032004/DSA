class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=-1
        for i in range(0,len(nums)):
            if nums[i]==0:
                j=i
                break
        if j==-1:
            return nums
        for i in range(j,len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums
        