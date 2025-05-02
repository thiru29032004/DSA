class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set()
        for num in nums:
            st.add(num)
        lon=0
        for num in st:
            if num-1 in st:
                continue
            else:
                x=num
                c=1
                while x+1 in st:
                    x=x+1
                    c+=1
                lon=max(lon,c)
        return lon
                


        