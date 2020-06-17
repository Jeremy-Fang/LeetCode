class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        heap = []
        N = len(nums)
        
        for i in range(N):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
                
        for i in dic.keys():
            if len(heap) < k:
                heapq.heappush(heap, (dic[i], i))
            else:
                if dic[i] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (dic[i], i))
                    
        return [item[1] for item in heap]
                
                    
