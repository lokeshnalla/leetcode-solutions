class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0          # Buy day (points to the current minimum price)
        profit = 0        # Stores the maximum profit

        # i represents the selling day
        for i in range(1, len(prices)):

            # Calculate profit if we buy on 'left' and sell on 'i'
            s = prices[i] - prices[left]

            # If profit is positive, update the maximum profit
            if s > 0:
                profit = max(profit, s)

            # If current price is less than or equal to buying price,
            # move the buying day to the current day
            else:
                left = i      # ✅ Correct (Don't use left += 1)

        return profit