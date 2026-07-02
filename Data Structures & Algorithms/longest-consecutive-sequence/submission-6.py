class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxLength = 0

        for num in nums:
            length = 1
            if (num - 1) not in setNums:
                while (length + num) in setNums:
                    length += 1
            maxLength = max(length, maxLength)

        return maxLength
