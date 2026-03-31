# Problem: Fibonacci Number
# Link: https://leetcode.com/problems/fibonacci-number/
# Approach: Iterative Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def fib(self, n: int) -> int:
        
        # Base cases
        if n < 2:
            return n
        
        # Initialize first two Fibonacci numbers
        a, b = 0, 1
        i = 1
        
        # Compute Fibonacci numbers iteratively
        while i < n:
            a, b = b, a + b
            i += 1
        
        return b