class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [(1,0),(0,1),(-1,0),(0,-1)]

        def invalid(r,c):
            return r < 0 or c < 0 or r >= N or c >= N

        visit = set()
        def dfs(r,c):
            if invalid(r,c) or not grid[r][c] or (r,c) in visit:
                return
            visit.add((r,c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)
        
        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        nr, nc = r + dr, c + dc
                        if invalid(nr, nc) or (nr,nc) in visit:
                            continue
                        if grid[nr][nc]:
                            return res
                        q.append((nr,nc))
                        visit.add((nr,nc))
                res += 1
            return res
        
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()