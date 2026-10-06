class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return false

        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m * n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # Get row, col so we can index into M
            i = mid // n
            j = (mid % n)

            print(f'(i,j){i} {j}')

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                lo = mid + 1
            else:
                hi = mid - 1
           

        return False
            

