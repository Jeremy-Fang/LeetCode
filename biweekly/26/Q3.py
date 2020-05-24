# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def trav(n, ma):
            if n:
                if n.val >= ma:
                    self.res += 1
                ma = max(ma, n.val)
                trav(n.left, ma)
                trav(n.right, ma)
                
        self.res = 1
            
        if not root:
            return 0
        
        trav(root.left, root.val)
        trav(root.right, root.val)
        
        return self.res
                
