class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        miss=k
        c=1
        while True:
            val=c*k
            if val not in nums:
                return val
            c+=1
        
            
            
        