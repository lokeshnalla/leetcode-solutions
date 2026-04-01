# Problem: Add Digits
# Link: https://leetcode.com/problems/add-digits/
# Approach: Repeated digit sum (simulation)
# Time Complexity: O(d) where d = number of digits
# Space Complexity: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        
        # Continue until number becomes a single digit
        while num >= 10:
            
            sum_digits = 0
            
            # Calculate sum of digits
            while num > 0:
                sum_digits += num % 10
                num //= 10
            
            # Update num with the digit sum
            num = sum_digits
        
        return num