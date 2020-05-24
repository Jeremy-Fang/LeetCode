# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        d = {}
        queue = [(root, 0, 0)]
        ma = 1
        
        if not root:
            return 0
        
        while queue:
            node, depth, pos = queue.pop(0)
            if node:
                if depth not in d:
                    d[depth] = pos
                else:
                      ma = max(ma, pos - d[depth] + 1)
                queue.append((node.left, depth + 1, pos * 2 + 1))
                queue.append((node.right, depth + 1, pos * 2 + 2))
                
        return ma
