class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        long = 0
        runTotal = 0

        for num in nums:
            if num == 1:
                runTotal += 1
            else:
                runTotal = 0

            long = max(long, runTotal)
        
        return long
        
            