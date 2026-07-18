class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary to group anagrams
        mp = {}

        # Traverse each word
        for i in strs:

            # Sort the word to create a common key
            b = "".join(sorted(i))

            # If key already exists,
            # append the word to its group
            if b in mp:
                mp[b].append(i)

            # Otherwise create a new list
            else:
                mp[b] = [i]

        # Return only the grouped lists
        return list(mp.values())