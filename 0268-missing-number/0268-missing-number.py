class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        S=0
        for num in nums:
            S+=num
        Sn=(n*(n+1))//2
        return Sn-S
        