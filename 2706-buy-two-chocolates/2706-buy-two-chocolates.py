class Solution(object):
    def buyChoco(self, prices, money):
        sorted_s=sorted(prices)
        min_cost = sorted_s[0]+sorted_s[1]
        if min_cost<=money:
            return money-min_cost
        return money

        