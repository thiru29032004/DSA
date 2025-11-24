class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        st=set()
        for num in nums:
            st.add(num)
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in st:
                ans.append(i)
        return ans
        