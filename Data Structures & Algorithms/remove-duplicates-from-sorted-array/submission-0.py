class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = set()
        k = 0
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] not in mySet:
                mySet.add(nums[i])
                k += 1
                i += 1
            else:
                nums.pop(i)
            length = len(nums)
        
        return k
