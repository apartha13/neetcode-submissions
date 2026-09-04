class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                curProf = prices[r] - prices[l]
                maxProf = max(curProf, maxProf)
            else:
                l = r
        
        return maxProf