class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set("AEIOUaeiou")
        arr=list(s)

        l=0
        r=len(s)-1
        while l<r:
            while l<r and arr[l] not in vowels:
                l+=1
            while l<r and arr[r] not in vowels:
                r-=1
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        return "".join(arr)
        