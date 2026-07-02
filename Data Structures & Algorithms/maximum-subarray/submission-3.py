class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        countSum = 0

        for num in nums:
            if countSum < 0:
                countSum = 0
            countSum += num
            maxSub = max(countSum, maxSub)
        
        return maxSub
        