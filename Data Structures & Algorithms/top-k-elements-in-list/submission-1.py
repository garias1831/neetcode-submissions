class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        for v in nums:
            counts[v] += 1
                
        pq = []
        heapq.heapify(pq)
        for val, count in counts.items():
            heapq.heappush(pq, (count, val))
            if len(pq) > k:
                heapq.heappop(pq)
        
       
        res = [v for c, v in pq]

        return res



        