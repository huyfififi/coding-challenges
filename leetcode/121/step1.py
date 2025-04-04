class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp_min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < tmp_min_price:
                tmp_min_price = price
                continue

            max_profit = max(max_profit, price - tmp_min_price)

        return max_profit
