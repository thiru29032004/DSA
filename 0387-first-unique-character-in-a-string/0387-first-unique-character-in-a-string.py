class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]][0]+=1
            else:
                hashmap[s[i]]=[1,i]
        for ch in hashmap:
            if hashmap[ch][0]==1:
                return hashmap[ch][1]
        return -1

        