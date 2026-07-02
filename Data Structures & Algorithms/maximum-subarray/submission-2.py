class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        countSum = 0

        for n in nums:
            if countSum < 0:
                countSum = 0
            countSum += n
            maxSum = max(maxSum, countSum)
        
        return maxSum