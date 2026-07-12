class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return []

        res = deque()
        l, r = 0, len(nums) - 1

        while l <= r:
            left = abs(nums[l])
            right = abs(nums[r])

            if left < right:
                res.appendleft(right ** 2)
                r -= 1
            else:
                res.appendleft(left ** 2)
                l += 1
        
        return list(res)