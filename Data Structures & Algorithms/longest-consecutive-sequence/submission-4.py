class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0

        for i, val in enumerate(nums):
            if val - 1 not in mySet:
                count = 1
                while val + count in mySet:
                    count += 1
                longest = max(longest, count)
        
        return longest