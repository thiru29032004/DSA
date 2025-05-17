class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    Sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if Sum==target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                    elif Sum>target:
                        l-=1
                    else:
                        k+=1
        return ans



        