class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mProf = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                mProf = max(prices[r] - prices[l], mProf)
            r += 1
        
        return mProf
