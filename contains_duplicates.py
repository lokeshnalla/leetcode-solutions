# Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Approach: Sort the array and check adjacent elements
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Sort the array so duplicates appear next to each other
        nums.sort()
        n = len(nums)
        
        # Check consecutive elements for duplicates
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        
        # If no duplicates found
        return False