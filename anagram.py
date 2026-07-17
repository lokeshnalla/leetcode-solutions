class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Dictionary to store the frequency of characters
        mp = {}

        # Count the frequency of each character in string 's'
        for ch in s:
            if ch in mp:
                # If character already exists, increment its count
                mp[ch] = mp[ch] + 1
            else:
                # Otherwise, add it with count 1
                mp[ch] = 1

        # Decrease the frequency for each character in string 't'
        for ch in t:
            # If character is not present, get() returns 0
            # Then subtract 1 from its count
            mp[ch] = mp.get(ch, 0) - 1

        # Check whether all frequencies became 0
        for i in mp.values():
            if i != 0:
                # If any count is not zero,
                # the strings are not anagrams
                return False

        # If all counts are zero,
        # both strings contain exactly the same characters
        return True