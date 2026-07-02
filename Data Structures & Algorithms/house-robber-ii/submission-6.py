class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0] if nums else 0
        
        firstNums = nums[1:]
        secondNums = nums[:-1]
        memo1 = [-1] * len(firstNums)
        memo2 = [-1] * len(firstNums)

        def dfs(i, length, arr, memo):
            if i >= length:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(arr[i] + dfs(i + 2, length, arr, memo), dfs(i + 1, length, arr, memo))
            return memo[i]
        
        return max(dfs(0, len(firstNums), firstNums, memo1), dfs(0, len(secondNums), secondNums, memo2))