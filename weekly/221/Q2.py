class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        d = collections.defaultdict(int)
        heap = []
        res = 0
        mx_day = 0
        
        for i in range(N):
            mx_day = max(mx_day, days[i]+i)
            
        i = 0
        
        while i < mx_day:                
            if i < N and apples[i]:
                heapq.heappush(heap, [days[i]+i-1,apples[i]])
            if heap:
                heap[0][1] -= 1
                res += 1
            
                if heap[0][1] == 0:
                    heapq.heappop(heap)
                
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            i += 1
        
        return res
