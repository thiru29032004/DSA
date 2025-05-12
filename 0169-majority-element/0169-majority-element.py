class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        me=None
        for i in range(n):
            if c==0:
                me=nums[i]
                c+=1
            elif nums[i]==me:
                c+=1
            else:
                c-=1
        return me

        