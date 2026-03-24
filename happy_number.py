# Problem: Happy Number
# Link: https://leetcode.com/problems/happy-number/
# Approach: Recursion with digit square sum
# Time Complexity: O(log n) per iteration
# Space Complexity: O(log n) due to recursion

class Solution:
    def isHappy(self, n: int) -> bool:
        
        sum = 0
        
        # If number becomes 1 or 7 → it is a happy number
        if n == 1 or n == 7:
            return True
        
        # If single digit but not 1 or 7 → not a happy number
        elif n < 10:
            return False
        
        else:
            # Compute sum of squares of digits
            while n > 0:
                temp = n % 10
                sum = sum + temp * temp
                n = n // 10
            
            # Recursively check the new number
            return self.isHappy(sum)