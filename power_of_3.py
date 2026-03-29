# Problem: Power of Three
# Link: https://leetcode.com/problems/power-of-three/
# Approach: Repeated division by 3
# Time Complexity: O(log₃ n)
# Space Complexity: O(1)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # Power of 3 must be positive
        if n < 1:
            return False
        
        # Keep dividing by 3 while divisible
        while n % 3 == 0:
            n //= 3
        
        # If we reach 1, it was a power of 3
        return n == 1