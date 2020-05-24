class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = collections.defaultdict(int)
        maj = len(arr)//2 + (len(arr)%2)
        if len(arr) % 2 == 0:
            maj = len(arr)//2
        for i in arr:
            d[i] += 1
            
        v = [i for i in sorted(d.values())]
        c = 0
        m = 0
        
        for i in range(len(v)-1, -1, -1):
            c += v[i]
            m += 1
            if c >= maj:
                return m
