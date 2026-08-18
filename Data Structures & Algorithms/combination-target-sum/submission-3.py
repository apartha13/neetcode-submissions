class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res = []

        def backtrack(path, tot, start):
            if tot > target:
                return

            if tot == target:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, tot + nums[i], i)
                path.pop()
            
            return
        
        backtrack([], 0, 0)
        return res