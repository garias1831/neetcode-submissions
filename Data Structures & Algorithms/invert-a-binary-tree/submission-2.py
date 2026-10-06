# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def inv(T):
            if T is None:
                return None
            if T.left is None and T.right is None:
                return TreeNode(T.val, None, None)

            return TreeNode(T.val, inv(T.right), inv(T.left))
        
        if root is None: return None
        return inv(root)