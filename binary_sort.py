class Solution:
    def search(self, nums: List[int], target: int):

        # Left pointer
        left = 0

        # Right pointer
        right = len(nums) - 1

        # Continue until the search space is empty
        while left <= right:

            # Find the middle index
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Target is in the left half
            elif target < nums[mid]:
                right = mid - 1

            # Target is in the right half
            else:
                left = mid + 1

        # Target not found
        return -1