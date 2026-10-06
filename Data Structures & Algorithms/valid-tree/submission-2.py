class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Idea - add each edge one at a time to build up the graph
        # As we build the graph, check for any cycles

        # At the end, run dfs on some arbitrary node to
        # Check connectedness

        # Edge case - single node
        if n == 1 and edges == []:
            return True

        seen = {}
        
        # Build the graph as a dict
        for (u, v) in edges:
            print(f'building... (u, v): ({u},{v})')
            # Seen both edges
            if u in seen and v in seen:
                return False

            # No self cycles
            if u == v:
                return False

            if u in seen:
                seen[u].add(v)
            else:
                seen[u] = set()
                seen[u].add(v)

            if v in seen:
                seen[v].add(u)
            else:
                seen[v] = set()
                seen[v].add(u)
        
        # Make sure we've at least touched every node
        if len(seen) != n:
            return False
        print('finished building')
        print(seen)
        # Run dfs on the graph to check connectedness
        marked = {}
        def dfs(v):
            visited = 0
            # For every neighbor
            for u in seen[v]:
                if u not in marked:
                    print(f'visiting u.. {u}')
                    marked[u] = True
                    visited += 1 + dfs(u)
            return visited
        visited = dfs(0)
        print(f'visited: {visited}')
        # Make sure the graph is connected     
        return visited == n
        