class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProf = 0

        while l < r and r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            maxProf = max(prices[r] - prices[l], maxProf)
            r += 1
        
        return maxProf
            
            