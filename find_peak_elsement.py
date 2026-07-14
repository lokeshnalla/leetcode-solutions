class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            # Peak is on the right side
            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            # Peak is on the left side (or at mid)
            else:
                right = mid

        return left