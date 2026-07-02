class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
           # print(count, r, c)
            if r == ROWS or c == COLS or min(r, c) < 0 or grid[r][c] == 0:
                return 0
            area = 1
            grid[r][c] = 0
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    print(area)
                    maxArea = max(maxArea, area)
                count = 0
        
        return maxArea
