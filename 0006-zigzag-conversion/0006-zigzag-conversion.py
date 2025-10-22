class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        n = len(s)
        b = [[" "]*n for _ in range(numRows)]
        
        i = 0
        j = 0
        down = True
        
        for ch in s:
            b[i][j] = ch
            if down:
                if i == numRows - 1:
                    down = False
                    i -= 1
                    j += 1
                else:
                    i += 1
            else:
                if i == 0:
                    down = True
                    i += 1
                else:
                    i -= 1
                    j += 1
        
        result = ""
        for r in range(numRows):
            for c in range(n):
                if b[r][c] != " ":
                    result += b[r][c]
        
        return result
