class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visit = set()
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if nr in range(ROWS) and nc in range(COLS) and ((nr, nc) not in visit) and (grid[nr][nc] == "1"):
                        visit.add((nr,nc))
                        q.append((nr,nc))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands