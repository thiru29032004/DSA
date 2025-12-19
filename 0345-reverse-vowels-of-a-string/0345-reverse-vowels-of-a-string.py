class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=["-1"]*len(s)
        vowels=""
        
        for i in range(len(s)):
            if s[i] not in "AEIOUaeiou":
                arr[i]=s[i]
            elif s[i]!=" ":
                vowels=s[i]+vowels
        j=0
        for i in range(len(s)):
            if arr[i]=="-1":
                arr[i]=vowels[j]
                j+=1
        return "".join(arr)


        