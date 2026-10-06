class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])


        dp = {} # dp (i, j) -> lip ending at M(i, j)
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(i, j, prevMatrixVal):
            if not (0 <= i < len(matrix)): return 0
            if not (0 <= j < len(matrix[0])): return 0
            # The increasing path rule here - means we don't ahve to
            # check the bounds of i + di and j + di
            if matrix[i][j] <= prevMatrixVal: return 0
            
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = 1
            for di, dj in dirs:
                dp[(i, j)] = max(
                    dp[(i, j)],
                    1 + dfs(i + di, j + dj, matrix[i][j])
                )
            return dp[(i, j)]

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
        
        return res

        
                
        


