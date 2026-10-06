class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # (i, j) -> True
        marked = dict()
        cells = 0
        srcs = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: srcs.append((i, j))
                if grid[i][j] > 0: cells += 1

        def bfs(sources):
            q = collections.deque(sources)
            q.append((-1, -1)) # Dummy token to indicate BFS tree depth
            res = 0

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while len(q) > 1:
                (i, j) = q.popleft()
                print("procing: ", i, j)
                if (i, j) in marked: continue

                # print(len(q))


                if (i, j) == (-1, -1):
                    res += 1
                    q.append((-1, -1))
                    continue
                
                print("nbord")
                for dx, dy in dirs:
                    # Bounds check
                    if ((0 <= i + dy and i + dy < m) and (0 <= j + dx) and (j + dx < n)):
                        # Valid cell
                        if grid[i + dy][j + dx] > 0:
                            q.append((i + dy, j + dx))
                print("nbors end")

                marked[(i, j)] = True
            
            return res - 1


        res = bfs(srcs)

        # print("len, ", len(marked))
        # edge cases for off-by-one time
        # if all rotting fruit 
        # and singleton 0  graph should return 0 apperantly
        if len(marked) == 1 and cells == 1: return 0
        if cells == 0: return 0

        
        return res if len(marked) >= cells else -1


                



            
        