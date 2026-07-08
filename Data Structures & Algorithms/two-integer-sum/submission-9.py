class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for i, val in enumerate(nums):
            if target - val in found:
                return [found[target - val], i]
            found[val] = i
        
        return []