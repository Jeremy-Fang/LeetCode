class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        N = len(arr)
        
        med = arr[(N - 1) // 2]
        d = collections.defaultdict(int)
        
        for i in range(N):
            d[arr[i]] = abs(arr[i] - med)
        
        arr.sort(key=lambda i:(-(d[i]-med), -i))
        
        return arr[:k]
