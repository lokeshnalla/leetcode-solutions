# Problem: Factorial Trailing Zeroes
# Link: https://leetcode.com/problems/factorial-trailing-zeroes/
# Approach: Count factors of 5

class Solution:
    def trailingZeroes(self, n: int) -> int:
        c=0
        while(n>0):
            n=n//5
            c=c+n
        return c