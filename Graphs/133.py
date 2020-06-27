"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        curr = None
        queue = [node]
        d = {}
        d[node.val] = Node(node.val, [])
        
        while queue:
            next_queue = []
            
            for item in queue:
                for neighbor in item.neighbors:
                    if neighbor.val not in d:
                        new = Node(neighbor.val, [])
                        d[item.val].neighbors.append(new)
                        d[new.val] = new
                        next_queue.append(neighbor)
                    else:
                        d[item.val].neighbors.append(d[neighbor.val])
                            
            queue = next_queue
            
        return d[node.val]
            
