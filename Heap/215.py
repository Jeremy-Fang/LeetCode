class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        
        for i in nums:
            if len(h) < k:
                heapq.heappush(h, i)
            else:
                if h[0] < i:
                    heapq.heappop(h)
                    heapq.heappush(h, i)
                
        return h[0]
