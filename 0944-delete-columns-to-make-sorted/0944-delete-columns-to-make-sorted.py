class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        mat=[list(string) for string in strs]
        res=0
        for i in range(len(mat[0])):
            s=[]
            for j in range(len(mat)):
                s.append(mat[j][i])
            k=sorted(s)
            if k!=s:
                res+=1
        return res


        