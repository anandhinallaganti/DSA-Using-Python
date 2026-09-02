class Solution(object):
    def maxProfit(self, prices):
        buy1=float("inf")
        profit1=0
        buy2=float("inf")
        profit2=0
        for i in prices:
            buy1=min(buy1,i)
            profit1=max(profit1,i-buy1)
            buy2=min(buy2,i-profit1)
            profit2=max(profit2,i-buy2)
        return profit2
        