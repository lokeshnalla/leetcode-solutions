class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        # Sort the array in ascending order
        nums.sort()

        # Product of the three largest numbers
        a = nums[-1] * nums[-2] * nums[-3]

        # Product of the two smallest numbers
        # and the largest number
        # This handles negative numbers
        b = nums[0] * nums[1] * nums[-1]

        # Return the maximum of both possibilities
        return max(a, b)