
import heapq
from collections import defaultdict

class DualHeap:
    def __init__(self):
        self.small = []  # Max heap (negative values)
        self.large = []  # Min heap

        self.delayed = defaultdict(int)

        self.small_size = 0
        self.large_size = 0

        self.small_sum = 0
        self.large_sum = 0

    def prune_small(self):
        while self.small:
            num = -self.small[0]

            if self.delayed[num] == 0:
                break

            heapq.heappop(self.small)
            self.delayed[num] -= 1

    def prune_large(self):
        while self.large:
            num = self.large[0]

            if self.delayed[num] == 0:
                break

            heapq.heappop(self.large)
            self.delayed[num] -= 1

    def rebalance(self):
        self.prune_small()
        self.prune_large()

        if self.small_size > self.large_size + 1:
            num = -heapq.heappop(self.small)

            self.small_size -= 1
            self.small_sum -= num

            heapq.heappush(self.large, num)

            self.large_size += 1
            self.large_sum += num

            self.prune_small()

        elif self.small_size < self.large_size:
            num = heapq.heappop(self.large)

            self.large_size -= 1
            self.large_sum -= num

            heapq.heappush(self.small, -num)

            self.small_size += 1
            self.small_sum += num

            self.prune_large()

    def add(self, num):
        self.prune_small()

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
            self.small_sum += num
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
            self.large_sum += num

        self.rebalance()

    def remove(self, num):
        self.prune_small()

        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.small_size -= 1
            self.small_sum -= num

            if num == -self.small[0]:
                self.prune_small()
        else:
            self.large_size -= 1
            self.large_sum -= num

            if self.large and num == self.large[0]:
                self.prune_large()

        self.rebalance()

    def cost(self):
        self.prune_small()
        self.prune_large()

        median = -self.small[0]

        return (
            median * self.small_size - self.small_sum
            + self.large_sum - median * self.large_size
        )


class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)

        # Required input variable
        maritovexi = nums

        # Part A: Calculate every window cost
        dh = DualHeap()

        for i in range(x):
            dh.add(maritovexi[i])

        costs = [dh.cost()]

        for right in range(x, n):
            dh.remove(maritovexi[right - x])
            dh.add(maritovexi[right])

            costs.append(dh.cost())

        # Part B: Dynamic programming
        INF = 10**18

        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0] = [0] * (n + 1)

        for t in range(1, k + 1):
            for i in range(1, n + 1):

                # Skip current element
                dp[t][i] = dp[t][i - 1]

                # Select a window ending at i - 1
                if i >= x:
                    dp[t][i] = min(
                        dp[t][i],
                        dp[t - 1][i - x] + costs[i - x]
                    )

        return dp[k][n]
