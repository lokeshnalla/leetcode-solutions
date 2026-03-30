# Problem: Perfect Number
# Link: https://leetcode.com/problems/perfect-number/
# Approach: Check divisors up to sqrt(num)
# Time Complexity: O(√n)
# Space Complexity: O(1)

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        # 1 is not a perfect number
        if num == 1:
            return False

        ans = 1  # Start with 1 since it is always a divisor

        # Check divisors from 2 to sqrt(num)
        for i in range(2, int(num**0.5) + 1):
            
            if num % i == 0:
                # Add both divisor and its pair
                ans += i + num // i

        # Check if sum of divisors equals the number
        return ans == num