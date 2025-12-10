class Solution:
    def findFirstPos(self,nums,index,target):
        while index>=0:
            if nums[index]==target:
                index-=1
            else:
                break
        return index+1
        
    def findLastPos(self,nums,index,target):
        while index<len(nums):
            if nums[index]==target:
                index+=1
            else:
                break
        return index-1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        last=-1
        l=0
        r=len(nums)-1

        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                first=self.findFirstPos(nums,m,target)
                last=self.findLastPos(nums,m,target)
                break
        return first,last
        