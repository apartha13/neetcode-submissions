class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(r, c, ROWS, COLS):
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            if text1[r] == text2[c]:
                memo[(r,c)] = 1 + dfs(r + 1, c + 1, ROWS, COLS)
            else:
                memo[(r, c)] = max(dfs(r + 1, c, ROWS, COLS), dfs(r, c + 1, ROWS, COLS))
            return memo[(r,c)]
        
        return dfs(0, 0, len(text1), len(text2))