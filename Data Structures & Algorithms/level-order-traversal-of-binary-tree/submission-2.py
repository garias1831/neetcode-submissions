# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # O(n) time and space, but inefficient
    # Ideally still do one pass
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        
        levels = []
        def inord(T, d):
            if T is None:
                return
            if len(levels) == d:
                levels.append([])

            inord(T.left, d + 1)

            # Current node
            levels[d].append(T.val)

            inord(T.right, d + 1)


        inord(root, 0)

        return levels


        