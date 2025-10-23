class Solution:
    def compressTheString(self,s1):
        res=""
        for i in range(len(s1)-1):
            val=int(s1[i])+int(s1[i+1])
            val%=10
            res=res+str(val)
        return res
    def hasSameDigits(self, s: str) -> bool:
        s1=s

        while len(s1)!=2:
            s1=self.compressTheString(s1)

        if(s1[0]==s1[1]):
            return True
        else:
            return False
        