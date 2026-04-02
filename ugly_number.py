# Problem: Ugly Number
# Link: https://leetcode.com/problems/ugly-number/
# Approach: Repeatedly divide by 2, 3, and 5
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isUgly(self, n: int) -> bool:
        
        # Continue dividing while n >= 1
        while n >= 1:
            
            # If n becomes 1, it is an ugly number
            if n == 1:
                return True
            
            # Divide by 2 if possible
            if n % 2 == 0:
                n //= 2
            
            # Divide by 3 if possible
            elif n % 3 == 0:
                n //= 3
            
            # Divide by 5 if possible
            elif n % 5 == 0:
                n //= 5
            
            # If not divisible by 2, 3, or 5 → not ugly
            else:
                return False
        
        return False