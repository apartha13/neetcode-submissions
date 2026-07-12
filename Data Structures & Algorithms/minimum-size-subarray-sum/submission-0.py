class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = math.inf
        rSum = nums[0]
        l, r = 0, 0

        while l <= r and r < len(nums):
            if rSum >= target:
                minSize = min(minSize, r - l + 1)
                rSum -= nums[l]
                l += 1
            else:
                if r + 1 in range(len(nums)):
                    rSum += nums[r + 1]
                r += 1
        
        return minSize if minSize != math.inf else 0