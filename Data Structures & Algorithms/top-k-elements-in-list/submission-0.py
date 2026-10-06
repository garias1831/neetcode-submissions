class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        for v in nums:
            counts[v] += 1
                
        pq = []
        heapq.heapify(pq)
        for val, count in counts.items():
            heapq.heappush(pq, (-count, val)) # Min heap: so largest |count| sits at the top
        
        # Max heap, then grab the top k
        res = []
        j = 0
        while j < k:
            count, val = heapq.heappop(pq)
            res.append(val)
            j += 1
        
        return res



        