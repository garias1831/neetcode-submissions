class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        seen = set()
        res = 0

        def bfs(si, sj):
            q = deque()
            q.append((si, sj))
            while len(q) > 0:
                (i, j) = q.popleft()

                dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for di, dj in dirs:
                    if ((i + di, j + dj)) in seen:
                        continue
                    
                    if 0 <= i + di and i + di < ROWS:
                        if 0 <= j + dj and j + dj < COLS and grid[i + di][j + dj] == '1':
                            q.append((i + di, j + dj))
                            seen.add((i + di, j + dj))

        # Count first time we see a 1, mark all contiguous ones    
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i, j) not in seen:
                    res += 1
                    seen.add((i, j))
                    bfs(i, j)

        return res
        