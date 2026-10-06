class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        print(f'{m}, {n}')

        # NOTE - for the future, prefer iterative DFS vs recursive
        # to avoid recursion depth errors on large test cases, esp for
        # n^2 type of ones where the depth ight be large relative to n
        visited = set() # (i, j)
        def dfs(i, j, level):
            if grid[i][j] > level:
                return False


            #print(f'{i}, {j}')
            # success
            visited.add((i, j))
            if i == m - 1 and j == n - 1:
                return True

            # out of bounds
            if not (0 <= i and i < m): return False
            if not (0 <= j and j < n): return False


            found = False
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for di, dj in dirs:
                if (i + di, j + dj) in visit: continue
                # oob for the traverse
                if not (0 <= (i + di) and (i + di) < m): continue
                if not (0 <= (j + dj) and (j + dj) < n): continue

                # height check for traverse
                if not (grid[i + di][j + dj] <= level): continue

                found = found or dfs(i + di, j + dj, level)

            return found
        

        def dfs_iterative(u, v, level):
            visit = {(u, v)}
            stack = [(u, v)]

            if grid[u][v] > level: return False

            while len(stack) > 0:
                (i, j) = stack.pop()

                if (i == m - 1 and j == n - 1): return True

                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for di, dj in dirs:
                    if (i + di, j + dj) in visit: continue
                    # oob for the traverse
                    if not (0 <= (i + di) and (i + di) < m): continue
                    if not (0 <= (j + dj) and (j + dj) < n): continue

                    # height check for traverse
                    if not (grid[i + di][j + dj] <= level): continue

                    # explore it
                    stack.append((i + di, j + dj))
                    visit.add((i + di, j + dj))
                
            return False

        # Binary search over all possible water levels

        bestlevel = max([max(row) for row in grid])
        hi = bestlevel
        lo = 0

        while lo <= hi:
            mid = lo + (hi - lo)//2 
            
            found = dfs_iterative(0, 0, mid)
            if found: # Can traverse with mid water level, try going lower
                hi = mid - 1
                bestlevel = mid
            else:
                lo = mid + 1 # could not traverse with this level, try going higher

        return bestlevel

        