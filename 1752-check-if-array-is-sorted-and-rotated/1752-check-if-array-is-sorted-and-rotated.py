class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]>nums[(i+1)%n]:
                count+=1
        if count<=1:
            return True
        else:
            return False
        