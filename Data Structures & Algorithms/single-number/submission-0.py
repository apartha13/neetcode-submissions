class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mySet = set()
        for num in nums:
            if num not in mySet:
                mySet.add(num)
            else:
                mySet.remove(num)
        return mySet.pop()
