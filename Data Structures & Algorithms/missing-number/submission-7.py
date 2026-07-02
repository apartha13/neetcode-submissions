class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sortNums = sorted(nums)

        for i in range(0, len(sortNums)):
            if i != sortNums[i]:
                return i
        
        return len(sortNums)