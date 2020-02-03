# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def s(n):
            if not n:
                return 0
            return n.val + s(n.left) + s(n.right)
        
        self.s = s(root)
        self.ans = float('-inf')
        
        def trav(n):
            if not n:
                return 0
            t = n.val + trav(n.left) + trav(n.right) #sum at point
            p = t * (self.s-t)
            if p > self.ans:
                self.ans = p
            return t
        
        trav(root)
        return self.ans%(10**9 + 7)
