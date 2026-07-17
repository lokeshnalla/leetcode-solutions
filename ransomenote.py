class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Dictionary to store the frequency of each character
        # required to construct the ransom note
        mp = {}

        # Count the frequency of each character in ransomNote
        for i in ransomNote:
            mp[i] = mp.get(i, 0) + 1

        # Traverse the magazine
        for i in magazine:

            # If the current character is needed,
            # reduce its required count
            if i in mp:
                mp[i] = mp[i] - 1

        # Assume we can construct the ransom note
        flag = True

        # Check if any character is still needed
        for j in mp.values():
            if j > 0:
                # Positive value means magazine didn't have
                # enough occurrences of that character
                flag = False

        # Return the result
        return flag