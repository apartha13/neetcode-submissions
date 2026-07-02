class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.countIslands(grid, r, c)
                    islands += 1
        return islands
    
    def countIslands(self, grid, r, c):
        ROWS, COLS = len(grid), len(grid[0])
        if (min(r, c) < 0 or 
        r == ROWS or c == COLS or 
        grid[r][c] == "0"):
            return
        grid[r][c] = "0"
        self.countIslands(grid, r + 1, c)
        self.countIslands(grid, r - 1, c)
        self.countIslands(grid, r, c + 1)
        self.countIslands(grid, r, c - 1)

