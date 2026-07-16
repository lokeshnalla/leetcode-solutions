class Solution:
    def maxVowels(self, s: str, k: int):

        # Count vowels in the first window
        count = 0
        for i in range(k):
            if s[i] in "aeiou":
                count += 1

        # Maximum vowels found so far
        ans = count

        # Slide the window
        for i in range(k, len(s)):

            # Remove the leftmost character of the previous window
            if s[i - k] in "aeiou":
                count -= 1

            # Add the new character entering the window
            if s[i] in "aeiou":
                count += 1

            # Update the maximum
            ans = max(ans, count)

        return ans