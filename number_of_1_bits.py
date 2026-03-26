# Problem: Number of 1 Bits
# Link: https://leetcode.com/problems/number-of-1-bits/
# Approach: Bit Manipulation (check each bit)
# Time Complexity: O(32) → O(1)
# Space Complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0  # Count of set bits
        
        # Check all 32 bits of the integer
        for i in range(32):
            res += (n & 1)   # Add 1 if last bit is 1
            n >>= 1          # Right shift to check next bit
        
        return res