class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = []

        for interval in intervals:

            # Current interval is completely before newInterval
            if interval[1] < newInterval[0]:
                ans.append(interval)

            # Current interval is completely after newInterval
            elif interval[0] > newInterval[1]:

                # Add newInterval first
                ans.append(newInterval)

                # From now on, treat current interval as newInterval
                newInterval = interval

            # Current interval overlaps with newInterval
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]

        # Add the final newInterval
        ans.append(newInterval)

        return ans