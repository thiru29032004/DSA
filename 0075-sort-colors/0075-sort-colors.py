class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        h=len(nums)-1
        m=0
        while m<=h:
            if nums[m]==1:
                m+=1
            elif nums[m]==2:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1
            elif nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
        return nums 
        