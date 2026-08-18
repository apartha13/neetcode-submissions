class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0

        if not prices or len(prices) == 1:
            return maxProf
        
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                maxProf = max(prices[r] - prices[l], maxProf)
                r += 1
            else:
                l = r
                r = r + 1
        
        return maxProf