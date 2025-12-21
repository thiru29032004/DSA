class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        Min = float('inf')

        while l <= r:
            mid = (l + r) // 2
            Min = min(Min, nums[mid])   

            if nums[mid] < nums[r]:
                r = mid - 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1   

        return Min
        