class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # Map unique char to (start, end)
        # idx of first place we find it, idx of last place we find it
        ranges = {}
        
        for i in range(len(s)):
            if s[i] not in ranges:
                ranges[s[i]] = (i, i)
            else:
                start, _ = ranges[s[i]]
                ranges[s[i]] = (start, i)
        
        res = []
        last = None
        for start, end in ranges.values():
            if not last:
                last = (start, end)
                continue

            last_start, last_end = last

            print(last, start, end)

            if start < last_end and last_end < end: # grow interval case
                last = (last_start, end)
            elif last_start < start and end < last_end: # nested interval case
                last = (last_start, last_end)
            else:
                res.append(last_end - last_start + 1)
                last = (start, end)
        # Dont forget last elem
        res.append(last[1] - last[0] + 1)
        return res
            

