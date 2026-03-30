class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        start = prices[0]
        for price in prices[1:]:
            profit = price - start

            if price < start:
                start = price

            maxProfit = max(maxProfit, profit)

        return maxProfit