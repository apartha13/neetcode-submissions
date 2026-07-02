class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        ans = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            ans[i] *= curr
            curr *= nums[i]

        curr = 1

        for i in range(len(nums)-1, -1, -1):
            ans[i] *= curr
            curr *= nums[i]
        
        return ans