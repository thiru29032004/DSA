class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        count=0
        s=0
        psm={}
        for i in range(0,n):
            s+=nums[i]
            if s==k:
                count+=1
            rem=s-k
            if rem in psm:
                count+=psm[rem]
            if s not in psm:
                psm[s]=1
            else:
                psm[s]+=1
        return count


        