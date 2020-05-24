# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.res = 0
        
        def trav(n, curr):
            curr[n.val] += 1
            if not n.left and not n.right:
                found = True
                odd = False
                for i in curr.keys():
                    if curr[i] % 2 == 1 and odd:
                        found = False
                    elif curr[i] % 2 == 1 and not odd:
                        odd = True
                if found:
                    self.res += 1
                curr[n.val] -= 1
                return
            
            if n.left:
                trav(n.left, curr)
            if n.right:
                trav(n.right, curr)
            curr[n.val] -= 1
            
        if not root:
            return 0
        
        
        trav(root, collections.Counter())
        
        return self.res
