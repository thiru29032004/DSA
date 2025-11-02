class Solution:
    def mark(self,grid,row,col,m,n):
        #east
        for j in range(col-1,-1,-1):
            if grid[row][j]!="W" and grid[row][j]!="G":
                grid[row][j]="1"
            else:
                break
        #west
        for j in range(col+1,n):
            if grid[row][j]!="W" and grid[row][j]!="G":
                grid[row][j]="1"
            else:
                break
        #north
        for i in range(row-1,-1,-1):
            if grid[i][col]!="W" and grid[i][col]!="G":
                grid[i][col]="1"
            else:
                break
        #south
        for i in range(row+1,m):
            if grid[i][col]!="W" and grid[i][col]!="G":
                grid[i][col]="1"
            else:
                break
        

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        grid=[[" "]*n for _ in range(m)]
        for wall in walls:
            grid[wall[0]][wall[1]]="W"
        
        for guard in guards:
            grid[guard[0]][guard[1]]="G"

        for guard in guards:
            row=guard[0]
            col=guard[1]
            self.mark(grid,row,col,m,n)
        
        c=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==" ":
                    c+=1
        return c

        
        


        