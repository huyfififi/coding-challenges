import math


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = math.inf
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
