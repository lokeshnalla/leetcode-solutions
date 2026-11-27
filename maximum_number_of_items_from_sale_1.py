from typing import List


class Solution:

  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    n = len(items)
    free = [0] * n

    # 1. Count free items unlocked by the first purchase of item i
    for i in range(n):
      f_i = items[i][0]
      for j in range(n):
        if i != j and items[j][0] % f_i == 0:
          free[i] += 1

    dp = [0] * (budget + 1)

    # 2. 0/1 Knapsack for the first purchase of each item (with free bonus)
    for i, (_, cost) in enumerate(items):
      gain = 1 + free[i]
      for b in range(budget, cost - 1, -1):
        if dp[b - cost] + gain > dp[b]:
          dp[b] = dp[b - cost] + gain

    # 3. Unbounded Knapsack for any additional copies (1 item per copy, using cheapest item)
    min_cost = min(cost for _, cost in items)
    for b in range(min_cost, budget + 1):
      if dp[b - min_cost] + 1 > dp[b]:
        dp[b] = dp[b - min_cost] + 1

    return max(dp)