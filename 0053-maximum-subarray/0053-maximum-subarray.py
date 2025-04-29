class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=float('-inf')
        s=0
        for num in nums:
            s+=num
            maxi=max(s,maxi)
            if s<0:
                s=0
        return maxi

        