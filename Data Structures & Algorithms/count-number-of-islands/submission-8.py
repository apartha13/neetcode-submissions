class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)

            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    island += 1
        
        return island