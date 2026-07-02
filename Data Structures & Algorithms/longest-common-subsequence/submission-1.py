class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        ROWS, COLS = len(text1), len(text2)
        def dfs(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r, c) in memo:
                return memo[(r,c)]
           
            if text1[r] == text2[c]:
                memo[(r, c)] = 1 + dfs(r + 1, c + 1)
            else:
                memo[(r, c)] = max(dfs(r + 1, c), dfs(r, c + 1))
                
            return memo[(r, c)]
        
        return dfs(0, 0)
