class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        n=len(nums)
        for j in range(1,n):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
        k=i+1
        return k
        