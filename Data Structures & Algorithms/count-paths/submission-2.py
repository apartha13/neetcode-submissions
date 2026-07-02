class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(r, c, ROWS, COLS):
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return 0
            if (r, c) in memo:
                return memo[(r,c)]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            memo[(r,c)] = dfs(r + 1, c, ROWS, COLS) + dfs(r, c + 1, ROWS, COLS)

            return memo[(r,c)]
        
        return dfs(0, 0, m, n)
        