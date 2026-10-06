class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # Djikstras - this doesn't fit the recomended cost bound
        # Guess:
        # Time: O(mk log(n))
        # Space: O(max(nk, n^2))

        # Build the graph
        graph = dict([(i, []) for i in range(n)])
        for (u, v, w) in flights:
            graph[u].append((v, w))


        # Idea - run djikstra, but keep track of
        # ALL previous distances as well as number of stops to get there
        # This way at the end we just pick out the smallest from dist[i]
        # each elem in dist[i] is a tuple (d, stopsleft)
        dist = dict([(i, []) for i in range(n)])
        dist[src].append((0, 0))

        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (0, src)) # (dist, vertex) 

        marked = dict()
        while len(pq) > 0:
            mindist, v = heapq.heappop(pq)
            marked[v] = True
            # 2. Update distance 
            for (u, w) in graph[v]:
                # For each current distance, update it and
                # The number of stops
                newmin_for_u = sys.maxsize
                for (found_dist, stops) in dist[v]:
                    newmin_for_u = min(found_dist + w, newmin_for_u)
                    dist[u].append((found_dist + w, stops + 1))

                if u not in marked:
                    heapq.heappush(pq, (newmin_for_u, u))
        
        # Extract the minimum distance
        res = sys.maxsize
        for (m, stopsleft) in dist[dst]:
            # If this didn't take too many edges and
            # The distance is minimized
            if stopsleft <= k + 1 and m < res:
                res = m
        # Couldn't find anything
        if res == sys.maxsize: return -1
        return res


