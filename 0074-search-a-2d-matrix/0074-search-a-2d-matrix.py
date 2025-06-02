class Solution:
    def search(self,matrix,target,row,m):
        l,h=0,m
        while l<=h:
            m=(l+h)//2
            if matrix[row][m]==target:
                return True
            elif matrix[row][m]<target:
                l=m+1
            else:
                h=m-1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n=len(matrix)
        m=len(matrix[0])

        for i in range(n):
            if matrix[i][0]<=target<=matrix[i][m-1]:
                if self.search(matrix,target,i,m-1):
                    return True
        return False

        


        