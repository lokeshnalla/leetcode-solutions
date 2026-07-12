class Solution:
    def searchRange(self, nums: List[int], target: int):

        # Initialize the left and right pointers for binary search
        left = 0
        right = len(nums) - 1

        # Perform binary search
        while left <= right:

            # Find the middle index
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:

                # Start both pointers from the found index
                l, r = mid, mid

                # Move left until the first occurrence is found
                while l >= 0 and nums[l] == target:
                    l -= 1

                # Move right until the last occurrence is found
                while r < len(nums) and nums[r] == target:
                    r += 1

                # Return the first and last occurrence
                return [l + 1, r - 1]

            # Search in the right half
            elif nums[mid] < target:
                left = mid + 1

            # Search in the left half
            else:
                right = mid - 1

        # Target not found
        return [-1, -1]