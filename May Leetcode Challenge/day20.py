# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.i = 1
        self.res = -1
        
        def trav(n):
            if n:
                trav(n.left)
                if self.i == k:
                    self.res = n.val
                    self.i += 1
                else:
                    self.i += 1
                    trav(n.right)

        trav(root)
        
        return self.res 
