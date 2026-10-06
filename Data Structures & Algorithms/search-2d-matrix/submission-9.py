class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False

        m = len(matrix)
        n = len(matrix[0])
        def ok(idx) -> bool:
            i, j = idx // n, idx % n
            # Idea -- will return true until the SMALLEST
            # The smallest here will be when matrix[i][j] == target in bisect left
            #
            if matrix[i][j] >= target:
                return True
            return False

        

        lo = 0
        hi = m * n - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ok(mid):
                hi = mid # bisect left means mid could be the answer
            else:
                lo = mid + 1 # mid definitel not the answer
        
        res = lo
        ir, jr = lo // n, lo % n
        
        if matrix[ir][jr] == target:
            return True
        return False
                
        