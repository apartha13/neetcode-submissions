class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        countSum = 0

        for n in nums:
            if countSum < 0:
                countSum = 0
            countSum += n
            maxSub = max(maxSub, countSum)
        
        return maxSub