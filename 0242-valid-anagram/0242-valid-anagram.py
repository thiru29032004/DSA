class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap1={}
        hashmap2={}
        for i in range(len(s)):
            hashmap1[s[i]]=hashmap1.get(s[i],0)+1
            hashmap2[t[i]]=hashmap2.get(t[i],0)+1
        
        for ch in hashmap1:
            if ch in hashmap2:
                if hashmap1[ch]!=hashmap2[ch]:
                    return False
            else:
                return False
        return True

        