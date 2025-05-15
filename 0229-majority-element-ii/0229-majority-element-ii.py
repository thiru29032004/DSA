class Solution(object):
    def majorityElement(self, nums):
        ele1=None
        ele2=None
        count1=0
        count2=0
        n=len(nums)
        for num in nums:
            if count1==0 and num!=ele2:
                ele1=num
                count1=1
            elif count2==0 and num!=ele1:
                ele2=num
                count2=1
            elif ele1==num:
                count1+=1
            elif ele2==num:
                count2+=1
            else:
                count1-=1
                count2-=1
        c1=0
        c2=0
        ans=[]
        for num in nums:
            if num==ele1:
                c1+=1
            if num==ele2:
                c2+=1
        if c1>(n//3):
            ans.append(ele1)
        if c2>(n//3):
            ans.append(ele2)
        return ans
            


        