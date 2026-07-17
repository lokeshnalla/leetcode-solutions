class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Set to store unique characters in the current window
        seen = set()

        # Left pointer of the sliding window
        left = 0

        # Stores the maximum length found so far
        count = 0

        # Right pointer moves through the string
        for i in range(len(s)):

            # If current character already exists in the window,
            # shrink the window from the left until it becomes unique
            while s[i] in seen:
                seen.remove(s[left])
                left = left + 1

            # Add the current character to the window
            seen.add(s[i])

            # Calculate the current window length
            c = i - left + 1

            # Update the maximum length
            count = max(c, count)

        # Return the length of the longest substring
        return count