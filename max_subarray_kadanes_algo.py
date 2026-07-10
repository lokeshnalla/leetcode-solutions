class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Current sum of the subarray
        curr_sum = nums[0]

        # Maximum subarray sum found so far
        max_sum = nums[0]

        # Traverse the array from the second element
        for i in range(1, len(nums)):

            # Decide whether to:
            # 1. Start a new subarray from nums[i]
            # 2. Extend the previous subarray
            curr_sum = max(nums[i], curr_sum + nums[i])

            # Update the maximum sum if current sum is larger
            max_sum = max(max_sum, curr_sum)

        # Return the maximum subarray sum
        return max_sum