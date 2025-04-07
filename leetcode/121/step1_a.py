class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        tmp_min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < tmp_min_price:
                tmp_min_price = prices[i]
                continue

            max_profit = max(max_profit, prices[i] - tmp_min_price)

        return max_profit
