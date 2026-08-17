class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        elif len(nums) < 2:
            return nums[0]

        noFir = nums[1:]
        noLas = nums[:-1]

        def dynamic(arr):
            if len(arr) < 2:
                return arr[0]
            dp = [-1] * (len(nums) - 1)
            dp[0], dp[1] = arr[0], max(arr[0], arr[1])

            for i in range(2, len(dp)):
                dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])
            
            return dp[-1]
        
        return max(dynamic(noFir), dynamic(noLas))