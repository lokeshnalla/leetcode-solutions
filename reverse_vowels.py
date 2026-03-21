# Problem: Reverse Vowels of a String
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # Set of vowels for quick lookup
        v = set("aeiouAEIOU")
        
        # Convert string to list (strings are immutable)
        s = list(s)
        
        l = 0
        r = len(s) - 1
        
        # Two-pointer approach
        while l < r:
            
            # Move left pointer until vowel is found
            while l < r and s[l] not in v:
                l += 1
            
            # Move right pointer until vowel is found
            while l < r and s[r] not in v:
                r -= 1
            
            # Swap vowels
            s[l], s[r] = s[r], s[l]
            
            # Move both pointers
            l += 1
            r -= 1
        
        # Convert list back to string
        return "".join(s)