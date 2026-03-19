# Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            res = max(res, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res