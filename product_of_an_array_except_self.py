# Problem: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Approach:
# 1. Count number of zeros in array
# 2. Compute product of all non-zero elements
# 3. Handle three cases:
#    - More than one zero → all outputs = 0
#    - Exactly one zero → only that index gets product, rest = 0
#    - No zeros → result[i] = total_product / nums[i]
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        a = 1        # Stores product of non-zero elements
        c = 0        # Count of zeros
        b = len(nums)

        # Step 1: Calculate product and count zeros
        for i in range(b):
            if nums[i] == 0:
                c += 1
            else:
                a = a * nums[i]

        d = [0] * b  # Result array

        # Step 2: Build result based on zero count
        for i in range(b):

            if c > 1:
                # If more than one zero → all elements will be 0
                d[i] = 0

            elif c == 1:
                # If exactly one zero
                if nums[i] == 0:
                    # Only index with zero gets the product
                    d[i] = a
                else:
                    d[i] = 0

            else:
                # No zeros → normal case
                d[i] = a // nums[i]

        return d