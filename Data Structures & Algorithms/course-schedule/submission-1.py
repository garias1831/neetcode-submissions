class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. build graph
        G = defaultdict(list)
        for u, v in prerequisites:
            G[u].append(v)
        
        marked = set()
        # For each source 
        for s in range(numCourses):
            if s in marked: continue

            # Run BFS starting at s
            marked_this_run = set()
            q = [s]
            while len(q) > 0:
                u = q.pop(0)
                for nb in G[u]:
                    # Cycle detected
                    if nb in marked_this_run:
                        return False

                    if nb not in marked:
                        q.append(nb)
    
                marked.add(u)
                marked_this_run.add(u)
    
        return True
