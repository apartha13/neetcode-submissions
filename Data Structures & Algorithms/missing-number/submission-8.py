class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        setNums = set(nums)

        for i in range(0, len(setNums)):
            if i not in setNums:
                return i
        
        return len(setNums)