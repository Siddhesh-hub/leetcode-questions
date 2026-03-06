class Solution:
    #Using kadanes algorithm
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
