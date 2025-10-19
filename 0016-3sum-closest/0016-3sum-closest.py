class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest=float('inf')
        n=len(nums)
        for i in range(n):
            l=i+1
            r=n-1
            
            while l<r:
                current_sum=nums[i]+nums[l]+nums[r]

                if abs(target-current_sum)< abs(target-closest):
                    closest=current_sum
                
                if current_sum==target:
                    return current_sum
                elif current_sum<target:
                    l+=1
                else:
                    r-=1
        return closest
                

                
        