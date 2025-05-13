class Solution(object):
    def ncr(self,n,r):
        res=1
        for i in range(r):
            res=res*(n-i)
            res=res//(i+1)
        return res
    def generate(self, numRows):
        ans=[]
        for row in range(1,numRows+1):
            temp=[]
            for i in range(row):
                k=self.ncr(row-1,i)
                temp.append(k)
            ans.append(temp)
        return ans


        
        