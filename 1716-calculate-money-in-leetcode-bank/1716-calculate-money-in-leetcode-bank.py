class Solution:
    def totalMoney(self, n: int) -> int:
        c=1
        savings=0
        dollor=1
        for day in range(1,n+1):
            if day%7==0:
                savings+=dollor
                c+=1
                dollor=c
            else:
                savings+=dollor
                dollor+=1
        return savings

        