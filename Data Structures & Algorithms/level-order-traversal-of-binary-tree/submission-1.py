# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        # 1. get depth of the tree
        def depth(T, d):
            if T is None:
                return -1

            return max(depth(T.left, d + 1), depth(T.right, d + 1), d)

        
        levels = [[] for _ in range(depth(root, 1))]

        def inord(T, d):
            if T is None:
                return

            inord(T.left, d + 1)

            # Current node
            levels[d].append(T.val)

            inord(T.right, d + 1)


        inord(root, 0)
        #

        return levels


        