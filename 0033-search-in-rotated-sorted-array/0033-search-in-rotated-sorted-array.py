class Solution:
    def search(self, nums: List[int], target: int) -> int:
            l = 0
            h = len(nums) - 1

            while l <= h:
                m = (l + h) // 2
                if nums[m] == target:
                    return m

                # Check if the left half is sorted
                if nums[l] <= nums[m]:
                    if nums[l] <= target < nums[m]:
                        h = m - 1
                    else:
                        l = m + 1
                else:  # Right half is sorted
                    if nums[m] < target <= nums[h]:
                        l = m + 1
                    else:
                        h = m - 1

            return -1

                