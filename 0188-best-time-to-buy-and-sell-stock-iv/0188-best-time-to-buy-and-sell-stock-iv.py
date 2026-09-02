class Solution(object):
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0

        n = len(prices)

        # If k >= n // 2, we can make as many transactions as we want (Stock II)
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # buy[t]: min effective cost into transaction t
        # sell[t]: max profit after completing transaction t
        buy = [float("inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for t in range(1, k + 1):
                buy[t] = min(buy[t], price - sell[t - 1])
                sell[t] = max(sell[t], price - buy[t])

        return sell[k]