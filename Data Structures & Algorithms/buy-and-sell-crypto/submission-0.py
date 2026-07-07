class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_st = prices[0]
        
        for i in prices:
            min_st = min(i, min_st)
            profit = i - min_st
            max_profit = max(max_profit, profit)

        return max_profit