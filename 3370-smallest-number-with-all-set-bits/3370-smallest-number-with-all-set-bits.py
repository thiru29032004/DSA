class Solution:
    def smallestNumber(self, n: int) -> int:
        nn=bin(n)[2:]
        flipN=""
        for ch in nn:
            if(ch=="0"):
                flipN=flipN+"1"
            else:
                flipN+=ch


        return int(flipN,2)
        