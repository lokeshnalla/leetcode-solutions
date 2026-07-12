class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort the intervals based on their starting value
        intervals.sort(key=lambda x: x[0])

        # This list will store the merged intervals
        l = []

        # Traverse each interval
        for i in intervals:

            # If the result list is empty
            # OR
            # the current interval does not overlap with the last merged interval
            if not l or i[0] > l[-1][1]:

                # Add the current interval to the result
                l.append(i)

            else:
                # Overlapping intervals
                # Merge them by updating the ending value
                # with the maximum ending value
                l[-1][1] = max(l[-1][1], i[1])

        # Return the merged intervals
        return l