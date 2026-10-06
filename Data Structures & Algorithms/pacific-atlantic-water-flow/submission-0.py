class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Idea - run bfs (or dfs) on every cell in the graph
        # Store two booleans, one for if we can reach pacific,
        # And one if we can reach the atlantic from this cell
        # We'll also use a hashmap to cache values that we've seen
        # And so we don't have to recompute all possible paths
        
        # Cache of (i, j) -> (reached_pacific, reached_atlantic)
        cache = dict()

        # ITERATIVE dfs - we CAN do this recursively too!
        # BUT bfs typically ITERATIVE
        def dfs(istart, jstart):
            # Add initial element to queue
            q = collections.deque()
            q.append((istart, jstart))

            # Map of marked nodes to avoid cycles
            marked = {}

            reached_pacific = False
            reached_atlantic = False
            while (len(q) > 0):
                i, j = q.popleft()
                marked[(i, j)] = True
                #print(q)
                print(f'(i, j): ({i},{j})')

                # Check if this node has a valid path from some
                # Previous iteration of the algo
                if (i, j) in cache:
                    prev_pac, prev_atl = cache[(i, j)]
                    reached_pacific = reached_pacific or prev_pac
                    reached_atlantic = reached_atlantic or prev_atl
                    continue

                # Check whether or not we've reached
                # The desired ocean
                if i == 0 or j == 0:
                    reached_pacific = True

                if (i == len(heights) - 1) or (j == len(heights[0]) - 1):
                    reached_atlantic = True

                # TODO: determine what to do if both are true
                if reached_pacific and reached_atlantic:
                    return (True, True)
                
                dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
                for (dx, dy) in dirs:
                    # Check out of bounds:
                    if ((0 <= i + dy and i + dy < len(heights)) and
                        (0 <= j + dx and j + dx < len(heights[0]))):
                        # We can only traverse in this direction
                        # If the height invariant is satisfied
                        if ((heights[i + dy][j + dx] <= heights[i][j]) and
                           ((i + dy, j + dx) not in marked)):
                                print(f' appending...(i, j): ({i + dy},{j + dx})')
                                q.append((i + dy, j + dx))
                
            return (reached_pacific, reached_atlantic)

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                
                print(f'PROCESSING ({i}, {j})')
                if (i, j) not in cache:
                    reached_pac, reached_atl = dfs(i, j)
                    cache[(i, j)] = (reached_pac, reached_atl)

                if cache[(i, j)] == (True, True):
                    res.append((i, j))
            
        return res
        
        