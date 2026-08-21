class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        # Sort the array
        nums.sort()

        ans = []

        # Check every pair of consecutive elements
        for i in range(1, len(nums)):

            # Start from the number after the previous element
            current = nums[i - 1] + 1

            # Add all missing numbers until nums[i]
            while current < nums[i]:
                ans.append(current)
                current += 1

        return ans