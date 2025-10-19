class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        lclosest=float('inf')
        rclosest=float('inf')
        n=len(nums)
        for i in range(n):
            l=i+1
            r=n-1
            
            while l<r:
                current_sum=nums[i]+nums[l]+nums[r]
                if current_sum==target:
                    return current_sum
                elif current_sum<target:
                    l+=1
                    if abs(target-current_sum)<abs(target-lclosest):
                        lclosest=current_sum
                else:
                    r-=1
                    if abs(target-current_sum)< abs(target-rclosest):
                        rclosest=current_sum
        diff1=abs(target-lclosest)
        diff2=abs(target-rclosest)
        if diff1<diff2:
            return lclosest
        else:
            return rclosest

                
        