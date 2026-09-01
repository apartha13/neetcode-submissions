class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0

        adj = {val: [] for val in range(n)}

        # get the adjacency lists
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        visit = set()
        
        def bfs(node, visit):
            q = deque()
            q.append(node)

            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
        
        conn = 0
        for i in range(n):
            if i not in visit:
                bfs(i, visit)
                conn += 1
        
        return conn
        
