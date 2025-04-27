class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        n=len(nums)
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in freq:
            if freq[num]>(n//2):
                return num

        