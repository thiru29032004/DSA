class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=0
        n,m=len(haystack),len(needle)
        start=-1
        while i<n and j<m:

            if haystack[i]==needle[j]:
                if start==-1:
                    start=i
                i+=1
                j+=1
                if j==m:
                    return start
            else:
                if start!=-1:
                    i=start+1
                    start=-1
                    j=0
                else:
                    i+=1
        
        return -1
        