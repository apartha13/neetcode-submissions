class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in neighbors:
                    nr = dr + row
                    nc = dc + col
                    if min(nr, nc) >= 0 and nr < ROWS and nc < COLS and (nr, nc) not in visit and grid[nr][nc] == "1":
                        q.append((nr, nc))

                    visit.add((nr, nc))
                

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visit and grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        
        return islands