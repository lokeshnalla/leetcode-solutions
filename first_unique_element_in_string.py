class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # Count frequency of each character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Find first character appearing only once
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1