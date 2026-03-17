# Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Approach: Reverse using string slicing

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        z=int(str(x)[::-1])
        if(x==z):
            return True
        else:
            return False 