class TimeMap:

    def __init__(self):
        # Key: str, val: list[str, int]
        self.kv = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv: return ""


        k_stamps = self.kv[key]
        
        # Binsearch over the timestamp to get largest value
        # Fuck this stupid edge case shit I literally know the algorithm,
        # but this fucking indexing shit pisses me off
        low = 0
        hi = len(k_stamps) - 1
        mid = low + (hi - low) // 2
        while (hi - low) > 1:
            mid = low + (hi - low) // 2
            e = k_stamps[mid]

            if e[1] == timestamp:
                return e[0]
            elif e[1] < timestamp:
                low = mid
            elif e[1] > timestamp:
                hi = mid
        # 2 items left now

        if timestamp >= k_stamps[0][1]:
            if k_stamps[hi][1] <= timestamp: return k_stamps[hi][0]
            else: return k_stamps[low][0] 


        return ""





        
