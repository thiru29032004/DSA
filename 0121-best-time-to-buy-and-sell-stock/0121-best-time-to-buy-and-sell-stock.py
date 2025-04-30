class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        minprice=float('inf')
        for curr_price in prices:
            minprice=min(minprice,curr_price)
            cost=curr_price-minprice
            if cost>profit:
                profit=cost
        return profit
        