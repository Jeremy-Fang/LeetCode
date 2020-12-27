class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        instances = collections.defaultdict(list)
        
        for i, lake in enumerate(rains):
            if lake != 0:
                instances[lake].append(i)
                
        heap = []
        res = []
        full = set()
        
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full:
                    return []
                full.add(lake)
                instances[lake].pop(0)
                if len(instances[lake]) > 0:
                    heapq.heappush(heap, (instances[lake][0], lake))
                res.append(-1)
            else:
                if len(full) and len(heap):
                    full.remove(heap[0][1])
                    res.append(heap[0][1])
                    heapq.heappop(heap)
                else:
                    res.append(1)
                
        return res
