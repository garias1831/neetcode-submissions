# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        nodes = []

        #Recursively search inorder, bc this is a BST, teh
        #Inorder traversal will be sorted arr
        def smallest(T):
            if T is None:
                return 



            smallest(T.left)
            nodes.append(T)
            smallest(T.right)

        smallest(root)

        return nodes[k - 1].val


            
            

        