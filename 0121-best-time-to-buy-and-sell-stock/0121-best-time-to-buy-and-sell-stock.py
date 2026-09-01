class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        max_profit = 0
        for i in prices:
            if i<buy:
                buy = i
            else:
                profit = i - buy
                max_profit = max(max_profit,profit)
        return max_profit

            

        