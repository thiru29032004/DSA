class Solution:
    def solve(self,col,mat,ld,ud,rowarr,ans,n):
        if col==n:
            ans.append([''.join(row) for row in mat])
            return
        for row in range(n):
            if ld[row+col]==0 and ud[n-1-row+col]==0 and rowarr[row]==0:
                mat[row][col]='Q'
                ld[row+col]=1
                ud[n-1-row+col]=1
                rowarr[row]=1
                self.solve(col+1,mat,ld,ud,rowarr,ans,n)
                mat[row][col]='.'
                ld[row+col]=0
                ud[n-1-row+col]=0
                rowarr[row]=0
    

    def solveNQueens(self, n: int) -> List[List[str]]:
        mat=[['.']*n for _ in range(n)]
        ld=[0]*(2*n-1)
        ud=[0]*(2*n-1)
        rowarr=[0]*n
        ans=[]
        self.solve(0,mat,ld,ud,rowarr,ans,n)
        return ans




        