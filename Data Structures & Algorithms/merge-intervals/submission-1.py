class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda iv: iv[0])

        res = []
        curr = intervals[0]
        for l, r in intervals:
            if curr[1] >= l:
                curr = [curr[0], max(r, curr[1])]
            else:
                res.append(curr)
                curr = [l, r]
        res.append(curr)
        
        return res



        