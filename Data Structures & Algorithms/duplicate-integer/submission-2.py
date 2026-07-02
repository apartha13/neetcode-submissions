class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()

        for i, val in enumerate(nums):
            if val in mySet:
                return True
            mySet.add(val)
        
        return False