class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        def memoization(r, c, rows, cols, cache, grid):
            if r >= rows or c >= cols or grid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            
            cache[r][c] = (memoization(r + 1, c, rows, cols, cache, grid) +
                           memoization(r, c + 1, rows, cols, cache, grid))
            
            return cache[r][c]

        return memoization(0, 0, ROWS, COLS, [[0] * COLS for i in range(ROWS)], obstacleGrid)