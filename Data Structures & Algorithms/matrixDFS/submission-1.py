class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1 or min(r, c) < 0:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            unique = 0
            visit.add((r,c))
            unique += dfs(r + 1, c)
            unique += dfs(r - 1, c)
            unique += dfs(r, c + 1)
            unique += dfs(r, c - 1)
            visit.remove((r,c))

            return unique
        
        return dfs(0,0)