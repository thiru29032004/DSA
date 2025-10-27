class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        values=[]
        for char in s:
            values.append(hashmap[char])
        
        for i in range(len(values)-1):
            if(values[i]< values[i+1]):
                values[i]=-1*values[i]
        return sum(values)



        