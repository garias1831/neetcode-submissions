class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        marked = [[False] * n for _ in range(m)]

        def search(i, j, k):
            if k == (len(word)): return True # found word

            # oob cases
            if not (0 <= i and i < m): return False
            if not (0 <= j and j < n): return False

            # Found a match
            if board[i][j] == word[k] and not marked[i][j]:
                marked[i][j] = True

                dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for (di, dj) in dirs:
                    found = search(i + di, j + dj, k + 1)
                    if found: return True
                
                # No path found - reset
                marked[i][j] = False

            return False
        
        for i in range(m):
            for j in range(n):
                if search(i, j, 0):
                    return True
        return False



