class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.dfs(r, c, rows, cols, grid)
                    islands += 1

        return islands

    def dfs(self, r, c, rows, cols, grid):
        if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        if grid[r][c] == '1':
            grid[r][c] = '0'
        
        self.dfs(r + 1, c, rows, cols, grid)
        self.dfs(r - 1, c, rows, cols, grid)
        self.dfs(r, c + 1, rows, cols, grid)
        self.dfs(r, c - 1, rows, cols, grid)
