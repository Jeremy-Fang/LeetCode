# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.low = L
        self.high = R
        self.total = 0
        
        def trav(n):
            if n:
                if n.val >= self.low and n.val <= self.high:
                    self.total += n.val
                if n.val > self.low:
                    trav(n.left)
                if n.val < self.high:
                    trav(n.right)
        
        trav(root)
        return self.total
