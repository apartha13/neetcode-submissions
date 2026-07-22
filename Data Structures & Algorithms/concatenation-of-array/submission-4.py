class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)
        ans = [0] * (len(nums) * 2)

        for num in nums:
            ans[l] = ans[r] = num
            l += 1
            r += 1

        return ans