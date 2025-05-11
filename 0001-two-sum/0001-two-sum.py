class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_set={}
        for i in range(0,len(nums)):
            val1=nums[i]
            val2=target-val1
            if val2 not in hash_set:
                hash_set[val1]=i
            else:
                return hash_set[val2],i

        


        