class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        Y = len(matrix)
        X = len(matrix[0])
        
        for i in range(Y):
            for j in range(X):
                heapq.heappush(heap, matrix[i][j])
                        
        while k > 1:
            heapq.heappop(heap)
            k -= 1
            
        return heap[0]
