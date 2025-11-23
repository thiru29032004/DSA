class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        st=set()
        for num in nums:
            if num in st:
                return [num,num+1]
            st.add(num)
        