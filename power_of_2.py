# Problem: Power of Two
# Link: https://leetcode.com/problems/power-of-two/
# Approach: Check all powers of 2 from 2^0 to 2^30
# Time Complexity: O(31) ≈ O(1)
# Space Complexity: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # Iterate through possible powers of 2
        for i in range(31):
            ans = 2 ** i
            
            # If any power equals n, then n is a power of two
            if ans == n:
                return True
        
        # If no match found
        return False