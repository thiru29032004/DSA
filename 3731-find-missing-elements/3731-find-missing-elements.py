class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        st=set()
        Min=float('inf')
        Max=float('-inf')
        for num in nums:
            st.add(num)
            Max=max(num,Max)
            Min=min(num,Min)
        res=[]
        for i in range(Min+1,Max):
            if i not in st:
                res.append(i)
        return res
            
        
        