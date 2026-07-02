class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        order = set(nums)

        for i in range(len(nums) + 1):
            if i not in order:
                return i
        
        return -1