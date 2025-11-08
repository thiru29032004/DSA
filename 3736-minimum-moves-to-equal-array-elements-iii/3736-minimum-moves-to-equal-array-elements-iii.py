class Solution:
    def minMoves(self, nums: List[int]) -> int:
        operation=0
        Max=max(nums)
        i=0
        while i<len(nums):
            if nums[i]!=Max:
                nums[i]+=1
                operation+=1
            else:
                i+=1
        return operation
                
            
        