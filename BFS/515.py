# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        queue = [(root, 0)]
        res = []
        
        while queue:
            node, level = queue.pop()
            
            if len(res) < level + 1:
                res.append(float('-inf'))
                
            res[level] = max(res[level], node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
                
        return res
