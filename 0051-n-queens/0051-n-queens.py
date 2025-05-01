class Solution:
    def isSafe(self, mat, row, col, n):
    # Check row on left side
        for c in range(col):
            if mat[row][c] == 'Q':
                return False

        # Check upper-left diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if mat[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Check lower-left diagonal
        r, c = row, col
        while r < n and c >= 0:
            if mat[r][c] == 'Q':
                return False
            r += 1
            c -= 1

        return True



    def solve(self,col,mat,n,ans):
        if col==n:
            ans.append(["".join(row) for row in mat])

            return 

        for row in range(n):
            if self.isSafe(mat,row,col,n):
                mat[row][col]='Q'
                self.solve(col+1,mat,n,ans)
                mat[row][col]='.'


    def solveNQueens(self, n: int) -> List[List[str]]:
        mat=[['.']*n for _ in range(n)]
        ans=[]
        self.solve(0,mat,n,ans)
        return ans