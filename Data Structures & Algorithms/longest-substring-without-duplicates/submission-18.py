class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            return 1 + (s[0] != s[1])

        l = 0
        seen = set()
        seen.add(s[l])
        maxLength = 1

        for r in range(1, len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            else:
                maxLength = max(maxLength, r - l + 1)
            seen.add(s[r])
        
        return maxLength