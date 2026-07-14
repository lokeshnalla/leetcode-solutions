class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        # Remove consecutive duplicates
        arr = []

        for num in nums:
            if not arr or arr[-1] != num:
                arr.append(num)

        count = 0

        # Check each middle element
        for i in range(1, len(arr) - 1):

            # Hill
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                count += 1

            # Valley
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                count += 1

        return count