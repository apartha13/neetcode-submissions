class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        rSum = 0

        for num in nums:
            if rSum < 0:
                rSum = 0
            rSum += num
            maxSub = max(maxSub, rSum)
        
        return maxSub