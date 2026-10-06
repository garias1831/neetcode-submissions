"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        marked = dict()

        def dfs(u):
            if u in marked:
                return marked[u]

            cpy = Node(u.val)
            marked[u] = cpy

            for v in u.neighbors:
                cpy.neighbors.append(dfs(v))
            
            return cpy
        
        return dfs(node) if node else None
                
                
            


        