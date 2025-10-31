class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashMap={}
        res=[]

        for num in nums:
            hashMap[num]=hashMap.get(num,0)+1
            if(hashMap[num]==2):

                res.append(num)
        return res
        