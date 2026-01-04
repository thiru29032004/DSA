class Solution:
    def findDivisor(self,num):
        Sum=0
        c=0
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                Sum+=i
                c+=1
                if num//i !=i:
                    Sum+=(num//i)
                    c+=1
            
        return Sum,c
        


    def sumFourDivisors(self, nums: List[int]) -> int:
        total=0
        for num in nums:
            Sum,divisor=self.findDivisor(num)
            if divisor==4:
                total+=Sum
        if total:
            return total
        else:
            return 0
        