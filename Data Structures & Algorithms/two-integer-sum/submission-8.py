class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}

        for i in range(len(nums)):
            if (target - nums[i]) in pair:
                return [pair[(target - nums[i])], i]
            pair[nums[i]] = i
        
        return [0]
