class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def memoization(r, c, rows, cols, grid):
            if min(r, c) < 0 or r >= rows or c >= cols:
                return 0
            if grid[r][c] != 0:
                return grid[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            
            grid[r][c] += memoization(r + 1, c, rows, cols, grid)
            grid[r][c] += memoization(r, c + 1, rows, cols, grid)
            
            return grid[r][c]
        
        return memoization(0, 0, m, n, [[0] * n for i in range(m)])
            
        