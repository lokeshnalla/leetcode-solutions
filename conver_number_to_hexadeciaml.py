# Problem: Convert a Number to Hexadecimal
# Link: https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# Approach: Built-in hex conversion
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num &= 0xFFFFFFFF
        return hex(num)[2:]