class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxLength = 0
        mySet = set()

        for i in range(len(s)):
            for k in range(i, len(s)):
                if s[k] in mySet:
                    break
                mySet.add(s[k])
            maxLength = max(maxLength, len(mySet))
            mySet.clear()

        return maxLength
