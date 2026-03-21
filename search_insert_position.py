# Problem: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Approach: Linear Scan
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # If target is less than or equal to first element
        if nums[0] >= target:
            return 0

        # Traverse array to find correct position
        for i in range(1, len(nums)):
            if nums[i-1] < target and nums[i] >= target:
                return i

        # If target is greater than all elements
        return len(nums)
    

# Problem: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Approach: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left