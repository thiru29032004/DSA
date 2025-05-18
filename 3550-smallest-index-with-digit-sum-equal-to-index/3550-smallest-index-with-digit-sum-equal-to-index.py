class Solution:
    def digitSum(self,n):
        sum=0
        while n>0:
            last_digit=n%10
            sum+=last_digit
            n//=10
        return sum
    def smallestIndex(self, nums: List[int]) -> int:
       
        n=len(nums)
        for i in range(n):
            sum=self.digitSum(nums[i])
            if sum==i:
                return i
        return -1
            
            
            
        