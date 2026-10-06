# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Idea - traverse the tree, but pass down the val of the
        # greatest ancestor to each of the children

        # k meaning the key of the largest ancestor
        def dfs(T, largest_ancestor_key):
            # Handle base cases

            if T == None:
                return 0


            num_good = 0

            # In this case, we found a good node, so add
            # it to the count
            if T.val >= largest_ancestor_key:
                num_good += 1

            # Repeat for each subchild
            num_good += dfs(T.left, max(T.val, largest_ancestor_key))
            num_good += dfs(T.right, max(T.val, largest_ancestor_key))
            return num_good
        
        # root val -1 because we always want to count the root
        return dfs(root, root.val)
        