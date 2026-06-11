class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l, r = 0, 0
        while l < len(prices) and r < len(prices):
            curr_profit = prices[r] - prices[l]
            if curr_profit > result:
                result = curr_profit
            if prices[l] > prices[r]:
                l, r = r, r + 1
            else:
                r += 1
        return result
            

        