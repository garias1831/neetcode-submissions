class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Mapping (i, j) to number of paths possible from that index
        cache = dict()

        def uniquePathsAt(i, j):
            # Out of bounds
            if (i > m - 1) or (j > n - 1):
                return 0

            # Bottom right corner
            if (i == m - 1) and (j == n - 1):
                return 1

            if ((i, j) in cache):
                return cache[(i, j)]

            numPathsRight = uniquePathsAt(i, j + 1)
            numPathsDown = uniquePathsAt(i + 1, j)
            cache[(i, j)] = numPathsRight + numPathsDown

            return numPathsRight + numPathsDown

        return uniquePathsAt(0, 0)
        