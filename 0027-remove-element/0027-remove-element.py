class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k=-1
        for i in range(len(nums)):
            if nums[i]==val:
                k=i
                break
        if(k==-1):
            return len(nums)
        
        for i in range(k+1,len(nums)):
            if nums[k]!=nums[i]:
                nums[k],nums[i]=nums[i],nums[k]
                k+=1
        return k
        