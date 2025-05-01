class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos_pos=0
        neg_pos=1
        n=len(nums)
        ans=[0]*n
        
        for i in range(0,n):
            if nums[i]>0:
                ans[pos_pos]=nums[i]
                pos_pos+=2
            else:
                ans[neg_pos]=nums[i]
                neg_pos+=2
        return ans
        