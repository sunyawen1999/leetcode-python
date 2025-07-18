# 121. Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Tags: Array, Dynamic Programming, Greedy

from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Track the lowest price so far, and compute the maximum profit
        if we sell at the current price.
        """
        min_price = inf
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
