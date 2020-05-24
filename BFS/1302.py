# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = [(root, 0)]
        s = 0
        depth = 0
        
        while q:
            
            if q[0][0] != None and q[0][1] != depth: # new level
                s = 0
            
            if q[0][0] == None:
                q.pop(0)
            else:
                node, depth = q.pop(0)
            
                if node: 
                    s += node.val
                    q.append((node.left, depth + 1))
                    q.append((node.right, depth + 1))
                        
        return s
