# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def trav(n,t):
            if not n.left and not n.right:
                return t-n.val == 0
            if n.left:
                if n.right:
                    return trav(n.left,t-n.val) or trav(n.right,t-n.val)
                return trav(n.left,t-n.val)
            return trav(n.right,t-n.val)
        
        if not root:
            return False
        return trav(root,sum)
