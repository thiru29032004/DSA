class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        hasharr=[0]*((n*n)+1)

        for i in range(n):
            for j in range(n):
                val=grid[i][j]
                hasharr[val]+=1
        
        miss=-1
        rep=-1
        for i in range(1,len(hasharr)):
            if hasharr[i]==0:
                miss=i
            elif hasharr[i]==2:
                rep=i
        return rep,miss

        