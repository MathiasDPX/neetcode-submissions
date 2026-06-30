class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0

        for i, buyPrice in enumerate(prices):
            for j, sellPrice in enumerate(prices[i:], i):
                profit = sellPrice - buyPrice
                if profit > bestProfit:
                    bestProfit = profit

        return bestProfit