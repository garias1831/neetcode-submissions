class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Build the graph
        graph = collections.defaultdict(lambda: set())

        for (u, v, w) in edges:
            graph[u].add((v, w)) # graph is directed
        
        print(graph)
        
        # Initialize distance array
        dist = dict([(i, -1) for i in range(n)])
        dist[src] = 0
        
        pq = []
        heapq.heappush(pq, (0, src)) # TODO: does this work with python
        marked = set()
        while len(pq) > 0:
            # Fetch the unmarked vertex with the smallest distance estimate
            # This is step 2., where we chooose the new vertex
            (best, v) = heapq.heappop(pq)
            if v in marked:
                continue
            marked.add(v)
            
            # For each neighbor of the vertex
            for (u, w) in graph[v]:
                # 1. Update the best estimate by looking at the neighbors
                newdist = dist[v] + w
                if newdist < dist[u] or dist[u] == -1:
                    dist[u] = newdist

                if u not in marked:
                    heapq.heappush(pq, (dist[u], u))
        
        return dist
            

        
            