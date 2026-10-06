class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        
        #BFS - modified to trav good
        def bfs(i, j): 
            q = deque()
            marked = set() #JUST the coords
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            #Want to keep track of the depth of the bfs tree
            q.append((i, j, 0))
            while len(q) > 0:
                (row, col, depth) = q.popleft()

                if depth < grid[row][col]:
                    grid[row][col] = depth


                #For each neighbor, add to the set
                for dx, dy in dirs:
                    #neighbor coord
                    nbor_row, nbor_col = row + dy, col + dx

                    #If not safe or visited
                    if not ((0 <= nbor_row and nbor_row < m) and
                        (0 <= nbor_col and nbor_col < n) and
                        ((nbor_row, nbor_col) not in marked)):
                        continue
                    elif grid[nbor_row][nbor_col] == -1:
                        continue #Impassable tile

                    q.append((nbor_row, nbor_col, depth + 1))
                    marked.add((nbor_row, nbor_col))

        #Run our modified bfs on all the treasure chest cells
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    print(i, j)
                    bfs(i, j)

                    


        