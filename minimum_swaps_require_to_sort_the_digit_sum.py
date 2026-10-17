
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        arr = []
        for i in range(n):
            digit_sum = sum(int(d) for d in str(nums[i]))
            arr.append((digit_sum, nums[i], i))

        arr.sort()

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
