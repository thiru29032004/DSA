class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        ans=[]
        word=""
        for i in range(n):
            if s[i]!=" ":
                word=word+s[i]
            elif i!=0 and s[i-1]!=" ":
                ans.append(word)
                word=""
        
        if word:
            ans.append(word)
        res=""
         
        for i in range(len(ans) - 1, -1, -1):
            res += ans[i]
            if i != 0:
                res += " "

        return res

        