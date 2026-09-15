class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for num in nums:
            length = 0

            if (num - 1) not in numSet:
                while num in numSet:
                    length += 1
                    num += 1
            
            maxLength = max(maxLength, length)
        
        return maxLength