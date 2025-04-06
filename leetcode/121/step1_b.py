class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        def find_max_profit(prices: list[int], day_i: int) -> tuple[int, int]:
            """Returns (max profit, min_price) up to day_i in prices."""
            if day_i == 0:
                return 0, prices[0]

            past_max_profit, past_min_val = find_max_profit(prices, day_i - 1)
            return (
                max(past_max_profit, prices[day_i] - past_min_val),
                min(prices[day_i], past_min_val),
            )

        return find_max_profit(prices, len(prices) - 1)[0]
