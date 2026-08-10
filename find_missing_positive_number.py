class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Convert the array into a set for fast lookup
        s = set(nums)

        # Start checking from the smallest positive integer
        i = 1

        # Keep checking until we find a missing number
        while i in s:
            i += 1

        return i