class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max=0
        count=0
        for digit in nums:
            if digit==1:
                count+=1
                if Max<count:
                    Max=count
            else:
                count=0
        return Max

            
        