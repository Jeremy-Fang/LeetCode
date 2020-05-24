# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def trav(n, val, d):
            if not n:
                return -1
            if n.val == val:
                return d + 1
            return max(trav(n.left, val, d + 1), trav(n.right, val, d + 1))
        
        def trav2(n, val, p):
            if not n:
                return -1
            if n.val == val:
                return p.val
            return max(trav2(n.left, val, n), trav2(n.right, val, n))
        
        return trav(root, x, 0) == trav(root, y, 0) and
    max(trav2(root.left, x, root), trav2(root.right, x, root)) !=
    max(trav2(root.left, y, root), trav2(root.right, y, root))
