# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        self.root = None
        
        def insert(val):
            
            def trav(n, val):
                
                if n.val > val:
                    if n.left:
                        trav(n.left, val)
                    else:
                        n.left = TreeNode(val)
                else:
                    if n.right:
                        trav(n.right, val)
                    else:
                        n.right = TreeNode(val)
                        
            if self.root == None:
                self.root = TreeNode(val)
                return
            
            trav(self.root, val)
            
        for node in preorder:
            insert(node)
            
        return self.root
