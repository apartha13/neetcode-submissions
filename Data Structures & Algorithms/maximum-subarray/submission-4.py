class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        rSum = 0

        for i, val in enumerate(nums):
            if rSum < 0:
                rSum = 0
            rSum += val
            maxSum = max(maxSum, rSum)

        return maxSum
