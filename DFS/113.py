# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        res = []
        stack = []
        
        def trav(n, t):
            nonlocal res 
            nonlocal stack
            if not n.left and not n.right:
                if t == n.val:
                    stack.append(n.val)
                    res.append(stack.copy())
                    stack.pop()
                return
            stack.append(n.val)
            if n.left:
                trav(n.left, t - n.val)
            if n.right:
                trav(n.right, t - n.val)
            stack.pop()
                
        if not root:
            return []
    
        trav(root, sum)
    
        return res
