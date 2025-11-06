class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=strs[0]
        for i in range(1,len(strs)):
            word=strs[i]
            j=0
            while j<len(word) and j<len(res) and  word[j]==res[j]:
                j+=1 
        
            res=word[:j]
        return res
            

        