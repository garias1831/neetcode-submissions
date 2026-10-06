class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS = len(board)
        COLS = len(board[0])
        # Each hashmap indexed by row or column
        row = defaultdict(set)
        col = defaultdict(set)
        blocks = defaultdict(set) 

        for i in range(ROWS):
            for j in range(COLS):
                cell = board[i][j]
                
                print(i, j)

                # Check rows and cols
                if cell != '.' and (cell in row[i] or cell in col[j]):
                    return False

                r = (i // 3)
                c = (j // 3)
                if cell != '.' and cell in blocks[3 * r + c]:
                    return False

                # Add to hashmaps
                if cell != '.':
                    row[i].add(cell)
                    col[j].add(cell)
                    blocks[3 * r + c].add(cell)                

        return True

                
                

        
        
        