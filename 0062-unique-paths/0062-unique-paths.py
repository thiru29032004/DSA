class Solution(object):
    def cp(self,i,j,m,n,dp):
        if i==(m-1) and j==(n-1):
            return 1
        if i>=m or j>=n:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j]= self.cp(i+1,j,m,n,dp) + self.cp(i,j+1,m,n,dp)
        return dp[i][j]
    def uniquePaths(self, m, n):
        i=0
        j=0
        dp=[[-1]*n for _ in range(m)]
        
               
        return self.cp(i,j,m,n,dp) 