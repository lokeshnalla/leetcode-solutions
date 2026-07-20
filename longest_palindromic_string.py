class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Variable to store the longest palindrome
        ans = ""

        # Function to expand around the center
        def expand(left, right):

            # Expand while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # Return the palindrome found
            return s[left + 1:right]

        # Try every index as a center
        for i in range(len(s)):

            # Odd length palindrome
            odd = expand(i, i)

            # Even length palindrome
            even = expand(i, i + 1)

            # Update the answer if a longer palindrome is found
            if len(odd) > len(ans):
                ans = odd

            if len(even) > len(ans):
                ans = even

        return ans