class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in neighbors:
                    nr = row + dr
                    nc = col + dc

                    if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visit and grid[nr][nc] == '1':
                        q.append((nr, nc))
                    visit.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        
        return islands