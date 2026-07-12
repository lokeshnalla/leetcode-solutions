class Solution:
    def subarraySum(self, nums: List[int], k: int):

        # Stores {prefix_sum : frequency}
        # Initially, prefix sum 0 has occurred once
        maps = {0: 1}

        # Stores the current prefix sum
        add = 0

        # Stores the number of subarrays whose sum equals k
        count = 0

        # Traverse through the array
        for i in range(len(nums)):

            # Update the prefix sum
            add += nums[i]

            # Check if there exists a previous prefix sum
            # such that (current_prefix - previous_prefix = k)
            if add - k in maps:

                # Add the frequency because there may be
                # multiple previous occurrences
                count += maps[add - k]

            # Store/update the frequency of the current prefix sum
            if add in maps:
                maps[add] += 1
            else:
                maps[add] = 1

        # Return the total number of subarrays
        return count