# Problem: Single Number
# Link: https://leetcode.com/problems/single-number/
# Approach: Bit Manipulation (XOR)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        unique = 0  # Initialize result
        
        # XOR all elements
        for i in nums:
            unique ^= i
        
        # Duplicate numbers cancel out, leaving the single number
        return unique